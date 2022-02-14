from decouple import config
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_pymongo import PyMongo


def config_app():
    _app = Flask(__name__)

    # SQL ACHEMY SETTINGS
    db_password = config('DB_PASSWORD')
    db_user = config('DB_USER')
    db_name = config('DB_NAME')
    _app.config['SECRET_KEY'] = config('SECRET_KEY')
    _app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{db_user}:{db_password}@localhost:5432/{db_name}"
    _app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # mongo settings
    _app.config["MONGO_URI"] = config('MONGO_URI')
    mongo = PyMongo(_app)

    _db = SQLAlchemy(_app)
    return _app, _db, mongo


def register_routes(_app):
    from routes import blueprints
    for blueprint in blueprints:
        _app.register_blueprint(blueprint)
    return _app