import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import  Migrate
from config import config_factory

db = SQLAlchemy()
migrage = Migrate()

from .views import graph_bp
from .models.models import Author, Book


def create_app():
    app = Flask(__name__)
    app_config = config_factory.get(
        os.environ.get('FLASK_ENV') or 'development')
    app.config.from_object(app_config)

    # Database initialization
    db.init_app(app)
    migrate = migrage.init_app(app, db)

    # Views
    app.register_blueprint(graph_bp)
    
    return app
