from flask import Flask
from .config import Config
from .db import db,migrate
# from .models import *
from .routes import student_bp
from .models import Student


def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    #initialize db
    db.init_app(app)
    migrate.init_app(app,db)

    #register blueprints
    app.register_blueprint(student_bp)

    return app