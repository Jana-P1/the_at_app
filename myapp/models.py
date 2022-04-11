#models 
from sqlite3 import DateFromTicks
from xml.etree.ElementTree import Comment
from myapp import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
#allows to set up isAuthenticate etc 
from flask_login import UserMixin
from datetime import datetime

#login management 
# allows us to use this in templates for isUser stuff 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(
        db.Integer, 
        primary_key=True
    )
    email = db.Column(
        db.String(64), 
        unique=True, 
        index=True
    )
    username = db.Column(
        db.String(64), 
        unique=True, 
        index=True
    )
    password_hash = db.Column(
        db.String(128)
    )
    stories = db.relationship(
        'SuccessStory',
        backref='author',
        lazy=True
    )

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

#going to use this in our login view 
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"Username {self.username}"

class SuccessStory(db.Model):
    __tablename__='success_stories'
    id = db.Column(
        db.Integer, 
        primary_key=True
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        nullable=False
    )
    title = db.Column(
        db.String(100),
        nullable=False
    )
    story = db.Column(
        db.String(500),
        nullable=False
    )
    date = db.Column(
        db.DateTime, 
        nullable=False, 
        default=datetime.utcnow
    )

    def __init__(self, title, story, user_id):
        self.title = title
        self.story = story
        self.user_id = user_id
    
    def __repr__(self):
        return f"Story ID: {self.id} --Date: {self.date} --- Title: {self.title}"


  


