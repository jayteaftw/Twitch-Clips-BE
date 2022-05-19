from BE import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    tag = db.relationship('Tag')

class Tag (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tags = db.Column(db.Strings(100000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Twitch_URL:
    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.String(500))
    date = db.Column(db.DateTime(timeZone=True), default=func.now())
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))



    