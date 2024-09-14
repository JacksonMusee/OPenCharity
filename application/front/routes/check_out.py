"""
This module contains functioalities for processing contribution payments
"""
from flask import Blueprint, render_template
from flask_login import login_required


check_out = Blueprint("check_out", __name__)


@check_out.route("/check-out/<int:project_id>/<string:project_title>", strict_slashes=False, methods=["GET", "POST"])
@login_required
def mpesa_check_out(project_id, project_title):
    """Process mpesa payments"""

    return render_template("front/check-out.html")