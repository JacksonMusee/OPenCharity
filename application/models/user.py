'''The module creates a model/database table to store users'''

from application import db
from datetime import datetime
from .project import Project
from .like import Like
from .bookmark import Bookmark
from .donation import Donation
from .comment import Comment
from flask_login import UserMixin


class User(db.Model, UserMixin):
    '''Ths is a blueprint for a user object'''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    dp = db.Column(db.String(64), nullable=False, default="default_dp.png")
    password = db.Column(db.String(64), nullable=False)

    # relationships
    likes = db.relationship("Like", backref="user", lazy=True)
    projects = db.relationship("Project", backref="author", lazy=True)
    bookmarks = db.relationship("Bookmark", backref="user", lazy=True)
    donations = db.relationship("Donation", backref="donor", lazy=True)
    comments = db.relationship("Comment", backref="user", lazy=True)

    def __repr__(self):
        '''Incase someone get curious and print a User object'''
        return f"User('{self.id}', '{self.username}')"
