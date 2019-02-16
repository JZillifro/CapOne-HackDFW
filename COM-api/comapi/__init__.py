# -*- coding: utf-8 -*-
import json
from functools import wraps
from flask import Flask, redirect, session
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_mongoengine import MongoEngine
from flask_uploads import (IMAGES, UploadSet, configure_uploads,
                           patch_request_class)
from flask_wtf.csrf import CSRFProtect

secrets = json.load(open('config.json'))

app = Flask(__name__)
app.config['BASE_FE_URL'] = secrets['BASE_FE_URL']
bcrypt = Bcrypt(app)
CORS(app)
csrf = CSRFProtect(app)

# app.config['MONGODB_SETTINGS'] = {
#     'db': '',
#     'host': secrets['mlab_host'],
#     'username': secrets['mlab_username'],
#     'password': secrets['mlab_password']
# }
app.config['MONGODB_SETTINGS'] = {
    'db': 'co-manager',
    'host': secrets['mlab_host'],
    'username': secrets['mlab_username'],
    'password': secrets['mlab_password']
}
db = MongoEngine(app)

from comapi.users.views import users_blueprint
# register blueprints

blueprints = [
    users_blueprint
]
for blueprint in blueprints:
    csrf.exempt(blueprint)
    CORS(blueprint)
    app.register_blueprint(blueprint)
