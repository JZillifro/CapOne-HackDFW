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

    savings = db.DecimalField(
        required = False,
        default = 0.0
    )

    checking = db.DecimalField(
        required = False,
        default = 0.0
    )

    credit = db.DecimalField(
        required = False,
        default = 0.0
    )

    user_limits = db.DecimalField(
        required = False,
        default = 600.0
    )
