'''
This module defines a route to create a new account
'''
from flask import render_template, Blueprint, url_for, redirect, flash
from ..forms.registration_fm import RegistrationForm
from application import bcrypt, db
from ...models.user import User


register_bp = Blueprint("register_bp", __name__)


@register_bp.route("/register", strict_slashes=False, methods=['GET', 'POST'])
def register():
    '''Renders th register page'''
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        new_user = User(username=form.username.data, email=form.username.data, password=hashed_pass)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration Successful", "success")
        return redirect(url_for("login_bp.login"))

    return render_template("front/register.html", form=form)
