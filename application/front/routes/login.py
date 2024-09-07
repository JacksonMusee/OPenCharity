'''
This module creates a route to manage login & sessions for a regular user
'''
from flask import render_template, Blueprint, request, redirect, url_for
from flask_login import login_user
from application import bcrypt
from ..forms.login_fm import LoginForm
from ...models.user import User


login_bp = Blueprint("login_bp", __name__)


@login_bp.route("/login", strict_slashes=False, methods=["GET", "POST"])
def login():
    '''Render login crdentials and logins in a user'''
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get("next")
            return redirect (next_page) if next_page else redirect(url_for("index_bp.index"))
    return render_template("front/login.html", form=form)