"""This modules defnes a form for posting new project"""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class ProjectForm(FlaskForm):
    """Project forms object blueprint"""
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    target = IntegerField("Target", validators=[DataRequired()])
    submit = SubmitField("Submit")
