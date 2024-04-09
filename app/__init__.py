# __init__.py

from flask import Flask
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager  # Import JWTManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/imdb'

mongo = PyMongo(app)
jwt = JWTManager(app)  # Initialize JWTManager with the Flask application

from app import auth, upload, view  # Import routes

# Use the routes
app.register_blueprint(auth.auth_bp)
app.register_blueprint(upload.upload_bp)
app.register_blueprint(view.view_bp)
