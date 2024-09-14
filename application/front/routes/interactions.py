"""
This module define how users interact with content
- Donate
- Comment on a project or a comment
- Like a project or a comment
- Bookmark a project
- Share a project
"""
from flask import Blueprint, render_template, redirect, url_for, flash
from application import db
from flask_login import login_required, current_user
from ..forms.comment_fm import CommentForm
from ...models.comment import Comment
from ...models.project import Project
from ...models.like import Like
from ...models.bookmark import Bookmark


interactions_bp = Blueprint("interactions_bp", __name__)


@interactions_bp.route("/project/<int:project_id>/comment", strict_slashes=False, methods=["GET", "POST"])
@login_required
def comment_project(project_id):
    """Process a comment on a project"""
    form = CommentForm()

    if form.validate_on_submit():
        try:
            new_comment = Comment(
                content=form.content.data,
                user_id=current_user.id,
                project_id=project_id)
            db.session.add(new_comment)
            project = Project.query.get(project_id)
            project.comment_count += 1
            db.session.commit()
            return redirect( url_for("project_bp.project_details", project_id=project_id))
        except Exception as e:
            db.rollback()
            form.errors["general"] = str(e)

    return render_template("front/index.html", comment_form=form)


@interactions_bp.route("/projects/<int:project_id>comments/<int:parent_id>/comment", strict_slashes=False, methods=["GET", "POST"])
@login_required
def comment_comment(project_id, parent_id):
    """Processess a comment on another comment"""
    form = CommentForm()

    if form.validate_on_submit():
        try:
            new_comment = Comment(
                content=form.content.data,
                user_id=current_user.id,
                project_id=project_id,
                parent_comment_id=parent_id)
            db.session.add(new_comment)
            parent = Comment.query.get(parent_id)
            parent.comment_count += 1
            db.session.commit()
            return redirect( url_for("project_bp.project_details", project_id=project_id, parent_comment_id=parent_id))
        except Exception as e:
            db.rollback()
            form.errors["general"] = str(e)
        return redirect( url_for("project_bp.project_details", project_id=project_id))


@interactions_bp.route("/projects/<int:project_id>/like", strict_slashes=False, methods=["GET", "POST"])
@login_required
def like_project(project_id):
    """Processess a like for a project"""
    already_liked = Like.query.filter_by(user_id=current_user.id, project_id=project_id).first()
    if not already_liked:
        try:
            new_like = Like(
                user_id=current_user.id,
                parent_type="Project",
                project_id=project_id)
            db.session.add(new_like)
            project = Project.query.get(project_id)
            project.like_count += 1
            db.session.commit()
        except Exception as e:
            db.session.rollback()
    else:
        flash("Yowzah, you can't like twice")

    return redirect(url_for("index_bp.index", _anchor=f"project-{project_id}"))


@interactions_bp.route("/comments/<int:project_id>/<int:comment_id>/like", strict_slashes=False, methods=["GET", "POST"])
@login_required
def like_comment(project_id, comment_id):
    """Processess a like for a comment"""
    already_liked = Like.query.filter_by(user_id=current_user.id, comment_id=comment_id).first()
    if not already_liked:
        try:
            new_like = Like(
            user_id=current_user.id,
            parent_type="Comment",
            comment_id=comment_id)
            db.session.add(new_like)
            comment = Comment.query.get(comment_id)
            comment.like_count += 1
            db.session.commit()            
        except Exception as e:
            db.session.rollback()
    else:
        flash("Yowzah, you can't like twice")

    return redirect(url_for("project_bp.project_details", project_id=project_id, _anchor=f"{comment_id}"))


@interactions_bp.route("/projects/<int:project_id>/bookmark", strict_slashes=False, methods=["GET", "POST"])
@login_required
def bookmark_project(project_id):
    """Processess a bookmark on a project"""
    already_bookmarked = Bookmark.query.filter_by(user_id=current_user.id, project_id=project_id).first()
    if not already_bookmarked:
        try:
            new_bookmark = Bookmark(
                user_id=current_user.id,
                project_id=project_id)
            db.session.add(new_bookmark)
            project = Project.query.get(project_id)
            project.bookmark_count += 1
            db.session.commit()
        except Exception as e:
            db.session.rollback()
    else:
        flash("Yoh, you already bookmarked this project")

    return redirect(url_for("index_bp.index", _anchor=f"project-{project.id}"))
