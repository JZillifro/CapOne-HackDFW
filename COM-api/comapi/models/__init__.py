import datetime

from comapi import db, secrets

class User(db.Document):
    meta = {'collection': 'Users'}

    c_id = db.StringField(
        required = True,
        default="",
    )

    name = db.StringField(
        required = False,
        default="Gary"
    )

    savings = db.ListField(
        required = False,
        default = ["id", 0.0]
    )

    checking = db.ListField(
        required = False,
        default = ["id", 0.0]
    )

    credit = db.ListField(
        required = False,
        default = ["id", 0.0]
    )

    user_limits = db.DecimalField(
        required = False,
        default = 600.0
    )

    password = db.StringField(
        required = True,
        default = "password1"
    )
