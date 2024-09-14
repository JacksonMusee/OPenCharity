from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate


db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    # app configurations. These can be moved to a class in separate file config.py and the class be
    # imported here, passed to this class and do app.config.from_object(Config)
    # In production, most of these should be set as evironment variables for security
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config["SECRET_KEY"] = "12341234"

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    @login_manager.user_loader
    def load_user(user_id):
        from application.models.user import User
        return User.query.get(int(user_id))

    from application.front.routes.index import index_bp
    from application.front.routes.login import login_bp
    from application.front.routes.register import register_bp
    from application.front.routes.logout import logout_bp
    from application.front.routes.project import project_bp
    from application.front.routes.interactions import interactions_bp
    from application.front.routes.check_out import check_out
    app.register_blueprint(index_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(logout_bp)
    app.register_blueprint(project_bp)
    app.register_blueprint(interactions_bp)
    app.register_blueprint(check_out)

    return app
