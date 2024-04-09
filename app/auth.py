from flask import Blueprint, render_template, redirect, url_for, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from validate_email import validate_email
from app import mongo

auth_bp = Blueprint('auth', __name__)

# Dummy user for demonstration purposes
users = {'test': 'test'}

@auth_bp.route('/', methods=['GET'])
def index():
    # Check if user is logged in by checking JWT token in cookies
    if 'access_token' in request.cookies:
        # User is logged in, redirect to dashboard
        return redirect(url_for('view.get_movies'))
    else:
        # User is not logged in, render login page
        return render_template('login.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic for POST requests
        data = request.form
        email = data.get('email')
        password = data.get('password')

        # Print received email and password for debugging
        print('Received email:', email)
        print('Received password:', password)

        # Check if user exists in the database and if the password matches
        user = mongo.db.users.find_one({'email': email})
        print('Retrieved user:', user)  # Print retrieved user for debugging
        if user and user['password'] == password:
            # Generate JWT token and set it as a cookie
            access_token = create_access_token(identity=email)
            response = redirect(url_for('view.get_movies'))
            response.set_cookie('access_token', access_token, httponly=True)
            return response

        return jsonify({'message': 'Invalid email or password'}), 401

    # Render login page for GET requests
    return render_template('login.html')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Handle signup logic for POST requests
        data = request.form
        email = data.get('email')
        password = data.get('password')
        confirm_password = data.get('confirm_password')

        # Check if email is valid
        is_valid = validate_email(email)
        if not is_valid:
            return jsonify({'message': 'Invalid email address'}), 400

        # Check if email is already registered
        if mongo.db.users.find_one({'email': email}):
            return jsonify({'message': 'Email is already registered'}), 400

        # Check if password matches confirmation
        if password != confirm_password:
            return jsonify({'message': 'Passwords do not match'}), 400

        # Add new user to database
        mongo.db.users.insert_one({'email': email, 'password': password})

        # Redirect to login page after successful signup
        return redirect(url_for('auth.index'))

    # Render signup page for GET requests
    return render_template('signup.html')

@auth_bp.route('/logout', methods=['GET'])
def logout():
    # Clear JWT token from cookies to logout the user
    response = redirect(url_for('auth.index'))
    response.set_cookie('access_token', '', expires=0)
    return response
