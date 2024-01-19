
# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config
from app.models import db  # Importa istanza di SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)  # Inizializza l'applicazione con l'istanza di SQLAlchemy
jwt = JWTManager(app)  # Inizializza il JWTManager con l'app Flask


from app import routes
