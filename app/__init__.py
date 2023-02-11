from flask import Flask
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

from app.config import config
from app.error_handlers import internal_server_error, page_not_found

db = SQLAlchemy()

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

    from app.main import main
    from app.auth import auth

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app

