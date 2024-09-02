'''This module defines the model/database table to store comments'''
from application import db
from datetime import datetime


class Comment(db.Model):
    '''This is the blueprint for Comment object'''
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)
    parent_comment_id = db.Column(db.Integer, db.ForeignKey("comment.id"), nullable=True)
    like_count = db.Column(db.Integer, nullable=False, default=0)

    # relationships
    parent = db.relationship("Comment", remote_side=[id], backref="children", lazy=True)

    def __repr__(self):
        '''Incase someone get curious and prints a Comment object'''
        return f"Comment('{self.id}', '{self.content}')"
