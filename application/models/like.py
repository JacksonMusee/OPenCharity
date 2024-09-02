'''This module defines a Model/Database table to store likes'''
from application import db
from datetime import datetime


class Like(db.Model):
    '''A  blueprint for a like object'''
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    parent_type = db.Column(db.String(16), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=True)
    comment_id = db.Column(db.Integer, db.ForeignKey("comment.id"), nullable=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        '''Incase someone prints this object'''
        return f"Like('{self.id}', '{self.date_created}')"
