from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

login_manager = LoginManager()

login_manager.login_view = "main.admin_login"


from app.models.admin import Admin


@login_manager.user_loader
def load_user(user_id):

    return Admin(user_id)


def create_app():

    app = Flask(__name__)

    app.config.from_object("config.Config")

    db.init_app(app)

    login_manager.init_app(app)

    from app.models.attack import Attack

    from app.routes.main_routes import main

    app.register_blueprint(main)

    with app.app_context():

        db.create_all()

    return app