import json
import time
import requests
from flask import jsonify, Response
from comapi.models import User
from flask import Blueprint, flash, jsonify, redirect, request, session, url_for

users_blueprint = Blueprint('users',
                               __name__,
                               url_prefix='/users')

current_user = None

@users_blueprint.route('/_createUser')
def create_user():
    customerId = '5c6858f86759394351bec029'
    apiKey = '8a1c3fd4fe7e739dd94b39699dd652cc'

    url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId,apiKey)
    payload = {
        "type": "Checking",
        "nickname": "test",
        "rewards": 10000,
        "balance": 1500,
    }
    # Create a Savings Account
    response = requests.post(
        url,
        data=json.dumps(payload),
        headers={'content-type':'application/json'},
    )
    return response.text
    #result = ['wow', 'cool']
    #return jsonify(result)

@users_blueprint.route('/_loadDB')
def load_database():
    customerId = '5c6858f86759394351bec029'
    apiKey = '8a1c3fd4fe7e739dd94b39699dd652cc'

    #url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customerId, apiKey)
    url = 'http://api.reimaginebanking.com/customers?key={}'.format(apiKey)
     # Get accounts
    response = requests.get(
        url,
        headers={'content-type':'application/json'},
    )

    customers = json.loads(response.text)
    for customer in customers:
        print(customer["first_name"])
        url = 'http://api.reimaginebanking.com/customers/{}/accounts?key={}'.format(customer["_id"], apiKey)
        actResponse = requests.get(
            url,
            headers={'content-type':'application/json'},
        )
        accts = {}

        accounts = json.loads(actResponse.text)
        for account in accounts:
            accts[account["type"]] = account
            print(account["type"])
        savings2 = ["id", 0.0]
        checking2 = ["id", 0.0]
        credit2 = ["id", 0.0]
        if "Savings" in accts:
            savings2[0] = accts["Savings"]["_id"]
            savings2[1] = accts["Savings"]["balance"]
        if "Checking" in accts:
            checking2[0] = accts["Checking"]["_id"]
            checking2[1] = accts["Checking"]["balance"]
        if "Credit Card" in accts:
            credit2[0] = accts["Credit Card"]["_id"]
            credit2[1] = accts["Credit Card"]["balance"]

        newCustomer = User(
            c_id = customer["_id"],
            name = customer["first_name"] + " " + customer["last_name"],
            savings = savings2,
            checking = checking2,
            credit = credit2,
            user_limits = 600.0,
            password = "password1"
        )

        newCustomer.save()
    return jsonify(customers)

@users_blueprint.route('/_login')
def login_credentials():
    global current_user
    #user = User.objects.get(name=request.form["username"], password=request.form["password"])
    user = User.objects.get(name='Jacques Champlin', password='password1')
    current_user = user
    return jsonify(current_user)

@users_blueprint.route('/_user-limit')
def set_user_limit():
    global current_user
    #current_user['user_limits'] = request.form["value"]
    current_user['user_limits'] = 2000
    current_user.save()
    return jsonify(current_user)

@users_blueprint.route('/_user-bills')
def get_leftover_cash():
    global current_user
    apiKey = '8a1c3fd4fe7e739dd94b39699dd652cc'

    balance = current_user['checking'][1]
    print(balance)
    url = 'http://api.reimaginebanking.com/accounts/{}/bills?key={}'.format(current_user['checking'][0], apiKey)
    billResponse = requests.get(
        url,
        headers={'content-type':'application/json'},
    )
    bills = json.loads(billResponse.text)
    for bill in bills:
        balance = balance - bill['payment_amount']
    current_user['checking'][1] = balance
    return jsonify(current_user)

# @posts_blueprint.route('/forum/<id>')
# def get_forum_data(id):
#     posts = Post.objects(f_ref=id)
#     result = [json.loads(post.to_json()) for post in posts]
#     for post in result:
#         post['_id'] = post['_id']['$oid']
#     sort = request.args.get('sort')
#     if sort == "buzz":
#         result = sorted(result, key=lambda post: post['up_votes'] + post['down_votes'] + post['comment_count'], reverse=True)
#     elif sort == "new":
#         result = sorted(result, key=lambda post: post['publish_date']['$date'], reverse=True)
#     else:
#         result = sorted(result, key=lambda post: post['up_votes'] - post['down_votes'], reverse=True)
#     return jsonify(result)
#
# @posts_blueprint.route('/<id>')
# def get_post_data(id):
#     post = json.loads(Post.objects.get(id=id).to_json())
#     post['_id'] = post['_id']['$oid']
#     return jsonify(post)
#
# @posts_blueprint.route('/downvote/<id>', methods=['POST', 'OPTIONS'])
# def downvote_post(id):
#     post = Post.objects.get(id=id)
#     votes = post['down_votes']
#     votes += 1
#     post['down_votes'] = votes
#     post.save()
#     return jsonify(votes)
#
# @posts_blueprint.route('/upvote/<id>', methods=['POST', 'OPTIONS'])
# def upvote_post(id):
#     post = Post.objects.get(id=id)
#     votes = post['up_votes']
#     votes += 1
#     post['up_votes'] = votes
#     post.save()
#     return jsonify(votes)
#
# @posts_blueprint.route('/new', methods=['POST', 'OPTIONS'])
# def new_one():
#     import pdb
#     if request.method == 'OPTIONS':
#         # pdb.set_trace()
#         resp = Response()
#         resp.headers['Access-Control-Allow-Origin'] = '*'
#         resp.headers['Access-Control-Allow-Methods'] = "POST, GET, OPTIONS"
#         resp.headers['Access-Control-Allow-Headers'] = "X-PINGOTHER, Content-Type"
#         resp.headers['Access-Control-Max-Age'] = "80000"
#         return resp
#     else:
#         # pdb.set_trace()
#         # title = request.form.get('title')
#         # text = request.form.get('text')
#         # image = request.form.get('image')
#         # forum = request.form.get('forum')
#
#
#         new_post = Post(
#             title = request.form.get('title'),
#             text = request.form.get('text'),
#             image = request.form.get('image'),
#             f_ref = request.form.get('f_ref')
#
#         )
#
#         forum = Forum.objects.get(id=request.form.get('f_ref'))
#         forum.post_count = forum.post_count + 1
#         forum.save()
#
#         # setattr(new_post, 'title', title)
#         # setattr(new_post, 'text', text)
#         # setattr(new_post, 'image', image)
#         # setattr(new_post, 'forum', forum)
#         # pdb.set_trace()
#
#         new_post.save()
#
#         return jsonify({'success': '200'})
