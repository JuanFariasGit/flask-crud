from flask import Flask
from .models import db
from flask_migrate import Migrate
from .views.index import main
import os

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/crud_flask'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.urandom(256)

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(main)

    return app