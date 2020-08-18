from flask import Flask
from .models import db
from flask_migrate import Migrate
from .views.index import main


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)

    app.config['SECRET_KEY'] = b'8d8ec0785a9bf876b84884f12fdca9e5'

    app.register_blueprint(main)

    return app