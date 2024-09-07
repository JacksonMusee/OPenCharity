"""
This module define how users interact with content
- Donate
- Comment on a project or a comment
- Like a project or a comment
- Share a project
- Bookmark a project
"""
from flask import Blueprint, render_template, redirect, url_for
from application import db
from flask_login import login_required, current_user
from ..forms.comment_fm import CommentForm
from ...models.comment import Comment
from ...models.project import Project


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

