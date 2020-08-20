from flask import Flask
from .models import db
from flask_migrate import Migrate
from .views.index import main


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(main)

    return app