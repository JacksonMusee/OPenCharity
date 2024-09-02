'''This module defines a Model/Database table to store bookmarks'''

from application import db
from datetime import datetime


class Bookmark(db.Model):
    '''A blueprint for a bookmark object'''
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        '''Incase someone prints a Bookmark object they see this'''
        return f"Bookmark('{self.id}', '{self.date_created}')"
