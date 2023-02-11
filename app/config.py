import os
from pathlib import Path


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(32))
    DB_NAME = os.getenv('DATABASE', 'test.db')

    BASE_DIR = Path(__file__).parent.parent
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", f"sqlite:///{BASE_DIR}/db.sqlite3")



    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
