from flask import render_template, Blueprint, url_for
from application.models.project import Project
from application.models.bookmark import Bookmark
from ..forms.comment_fm import CommentForm
from flask_login import login_required, current_user

index_bp = Blueprint("index_bp", __name__)


@index_bp.route("/", defaults={"filter": None})
@index_bp.route("/<string:filter>", strict_slashes=False)
def index(filter):
    '''Returns the home page'''
    comment_form = CommentForm()

    if filter == "trending":
        raw_projects = Project.query.order_by(Project.date_created.desc()).limit(10).all()
        projects = sorted(raw_projects, key=lambda x: (x.like_count + x.comment_count + x.donation_count), reverse=True)
    else:
        projects = Project.query.order_by(Project.date_created.desc())
    return render_template("front/index.html", projects=projects, comment_form=comment_form)


@index_bp.route("/bookmarks", strict_slashes=False)
@login_required
def get_bookmarks():
    """Fetch all projects a user has bookmarked"""
    comment_form = CommentForm()

    user_bookmarks = Bookmark.query.filter_by(user_id=current_user.id).order_by(Bookmark.date_created.desc()).all()
    projects = []
    for bookmark in user_bookmarks:
        projects.append(bookmark.project)

    return render_template("front/index.html", projects=projects, comment_form=comment_form)


@index_bp.route("/initiatives", strict_slashes=False)
@login_required
def get_initiatives():
    """Fetch all projects of a user"""
    comment_form = CommentForm()

    user_initiatves = Project.query.filter_by(author_id=current_user.id).order_by(Project.date_created.desc()).all()
    projects = user_initiatves

    return render_template("front/index.html", projects=projects, comment_form=comment_form)
