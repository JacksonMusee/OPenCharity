from application import db
from datetime import datetime
from .comment import Comment
from .bookmark import Bookmark
from .donation import Donation


class Project(db.Model):
    '''Project object'''
    id = db.Column(db.Integer, primary_key=True,)
    title = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    target = db.Column(db.Integer, nullable=False)
    raised = db.Column(db.Integer, nullable=False, default=0)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.String(12), nullable=False, default="Pending")
    date_approved = db.Column(db.DateTime, nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    comment_count = db.Column(db.Integer, nullable=False, default=0)
    bookmark_count = db.Column(db.Integer, nullable=False, default=0)
    like_count = db.Column(db.Integer, nullable=False, default=0)
    donation_count = db.Column(db.Integer, nullable=False, default=0)

    # Relationship with other models
    comments = db.relationship("Comment", backref="project", lazy=True)
    bookmarks = db.relationship("Bookmark", backref="project", lazy=True)
    donations = db.relationship("Donation", backref="project", lazy=True)

    def __repr__(self):
        '''Incase someone prints this object they see this'''
        return f"Project('title': '{self.title}', 'date_approved': '{self.date_approved}')"