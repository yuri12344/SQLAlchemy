from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from environs import Env
from app import views

env = Env()
env.read_env()
db = SQLAlchemy()

def create_app() -> Flask:  
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yuri:admin@localhost:5432/local'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    app.db = db

    Migrate(app, db)
    views.init_app(app)
    return app