# app/__init__.py
import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register blueprints
    # Import blueprints *after* db is initialized but before create_all
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
