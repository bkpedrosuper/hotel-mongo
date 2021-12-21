
from flask import Flask, render_template
from decouple import config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


def config_app(_app):
    db_password = config('DB_PASSWORD')
    db_user = config('DB_USER')
    db_name = config('DB_NAME')
    _app.config['SECRET_KEY'] = config('SECRET_KEY')
    _app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{db_user}:{db_password}@localhost:5432/{db_name}"
    _app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    _db = SQLAlchemy(app)
    return _app, _db


def register_routes(_app):
    from routes import blueprints
    for blueprint in blueprints:
        _app.register_blueprint(blueprint)
    return _app


app, db = config_app(app)
app = register_routes(app)


@app.route('/')
def initiate():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
