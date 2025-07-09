# app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_ckeditor import CKEditor, CKEditorField

class Base(DeclarativeBase):
    pass

db= SQLAlchemy(model_class=Base)
ckeditor = CKEditor()

def create_app():
    app = Flask(__name__, instance_relative_config=True)  # Enable instance folder


    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass  # Already exists

    # Define DB path relative to instance folder for better portability
    app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
    db_path = os.path.join(app.instance_path, "atn.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Optional: Disable modification tracking

    """initialize app extensions"""
    db.init_app(app)
    ckeditor.init_app(app)

    # Register blueprints
    # Import blueprints *after* db is initialized but before create_all
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Create tables within the application context
    with app.app_context():
        # Import models *inside* the context and after db is initialized
        db.create_all()

    return app
