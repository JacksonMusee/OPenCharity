"""This module defines tools for managing user logouts"""
from flask import Blueprint, redirect, url_for
from flask_login import logout_user


logout_bp = Blueprint("logout_bp", __name__)


@logout_bp.route("/logout")
def logout():
    """Logs out a user"""
    logout_user()
    return redirect(url_for("login_bp.login"))
