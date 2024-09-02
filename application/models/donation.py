'''This module defines a model/database table to store donation transactions'''
from application import db
from datetime import datetime


class Donation(db.Model):
    '''This is a blueprint for a donation object'''
    id = db.Column(db.Integer, primary_key=True)
    gateway = db.Column(db.String(32), nullable=False)
    reference_code = db.Column(db.String(120), nullable=False)
    donor_name = db.Column(db.String(64), nullable=False, default="Anonymous")
    amount = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False, default=0)
    transaction_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        '''Incase someone get curous and prints a Donation object they see this'''
        return f"Donation('{self.id}', '{self.gateway}', '{self.amount}')"
