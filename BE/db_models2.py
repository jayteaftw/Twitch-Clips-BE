from __init__ import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    tags = db.Column(db.Strings(100000))
    #tag = db.relationship('Tag')
    '''
    id  email           password     tags               vgwijbjksdf
    ________________________________________________________________________
    1 | test@gmail.com | password | "VALORANT, DOTA" | token
    '''


'''
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email =  db.Column(db.String(150), db.ForeignKey('user.email')
    tags = db.Column(db.Strings(100000))
    
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
'''


class Twitch_URL:
    id = db.Column(db.Integer, primary_key = True)
    tag = db.Column(db.String(500))
    url = db.Column(db.String(500))
    date = db.Column(db.DateTime(timeZone=True), default=func.now())
    #tags = db.Column(db.Integer, db.ForeignKey('tag.id'))
    '''
    id  tag               url           date
    ________________________________________________________
    1 | VALORANT | http://twitch... | 2022-05-22T20:53:31Z 
    '''



    