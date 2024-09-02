'''
This module defines a route to create a new account
'''
from flask import render_template, Blueprint


register_bp = Blueprint("register_bp", __name__)


@register_bp.route("/register", strict_slashes=False)
def register():
    '''Renders th register page'''
    return render_template("front/register.html")
