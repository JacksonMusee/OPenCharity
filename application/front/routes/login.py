'''
This module creates a route to manage login & sessions for a regular user
'''
from flask import render_template, Blueprint
from ..forms.login_fm import LoginForm


login_bp = Blueprint("login_bp", __name__)


@login_bp.route("/login", strict_slashes=False)
def login():
    '''Render login crdentials and logins in a user'''
    form = LoginForm()
    return render_template("front/login.html", form=form)
