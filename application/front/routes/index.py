from flask import render_template, Blueprint, url_for
from application.models.project import Project

index_bp = Blueprint("index_bp", __name__)


@index_bp.route("/index", strict_slashes=False)
@index_bp.route("/", strict_slashes=False)
def index():
    '''Returns the home page'''
    projects = Project.query.all()
    return render_template("front/index.html", projects=projects)


@index_bp.route("/project/<int:project_id>", strict_slashes=False)
def project_details(project_id):
    '''Returns detailed view of a project'''
    project = Project.query.get(project_id)
    return render_template("front/project_details.html", project=project)
