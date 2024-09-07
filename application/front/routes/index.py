from flask import render_template, Blueprint, url_for
from application.models.project import Project
from ..forms.comment_fm import CommentForm

index_bp = Blueprint("index_bp", __name__)


@index_bp.route("/index", strict_slashes=False)
@index_bp.route("/", strict_slashes=False)
def index():
    '''Returns the home page'''
    comment_form = CommentForm()
    projects = Project.query.order_by(Project.date_created.desc())
    return render_template("front/index.html", projects=projects, comment_form=comment_form)
