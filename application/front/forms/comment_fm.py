"""This module defines a form used make a comment"""
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    """Comment form object class"""
    content = TextAreaField("Content", validators=[DataRequired()])
    submit = SubmitField("Comment")