"""
This module defines logic to handle all operations related to a project
- Post new project
- Update
- Delete
"""
from flask import Blueprint, render_template, redirect, url_for
from application import db
from ..forms.project_fm import ProjectForm
from ..forms.comment_fm import CommentForm
from ...models.project import Project
from flask_login import login_required, current_user
import os

project_bp = Blueprint("project_bp", __name__)


@project_bp.route("/new-project", strict_slashes=False, methods=["GET", "POST"])
@login_required
def new_project():
    """Handles creating a new project"""
    form = ProjectForm()

    if form.validate_on_submit():
        try:
            new_project = Project(
                title=form.title.data,
                content=form.content.data,
                target=form.target.data,
                author_id=current_user.id)
            db.session.add(new_project)
            db.session.commit()
            return redirect(url_for("index_bp.index"))
        except Exception as e:
            db.session.rollback()
            form.errors["general"] = str(e)            
    return render_template("front/project.html", form=form)


@project_bp.route("/project/<int:project_id>", strict_slashes=False)
def project_details(project_id):
    '''Returns detailed view of a project'''
    comment_form = CommentForm()
    project = Project.query.get(project_id)
    return render_template("front/project_details.html", project=project, comment_form=comment_form)