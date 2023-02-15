from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail

from app.config import config
from app.error_handlers import internal_server_error, page_not_found

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_name='default'):
    app = Flask(__name__)
    app.static_folder = 'static'
    app.config.from_object(config[config_name])


    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)

    Bootstrap(app)

    csrf = CSRFProtect(app)
    csrf.init_app(app)
    app.config['CSRF'] = csrf

    db.init_app(app)

    login_manager.init_app(app)

    mail.init_app(app)

    from app.main import main
    from app.auth import auth
    from app.posts import posts

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(posts)

    return app
