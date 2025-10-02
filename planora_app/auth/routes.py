# planora_app/auth/routes.py
from flask import render_template, request, redirect, url_for, session, flash
from planora_app.auth import auth_bp
from planora_app import mongo
import bcrypt
from bson.objectid import ObjectId

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = mongo.db.users.find_one({'email': email})
        # user['password'] should be the hashed password (bytes/binary)
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
            session['user_id'] = str(user['_id'])
            session['username'] = user.get('username')
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))  # app-level route
        else:
            flash('Invalid email or password', 'danger')

    return render_template('auth/login.html')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if password != confirm_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('auth.signup'))

        if mongo.db.users.find_one({'email': email}):
            flash('Email already registered', 'danger')
            return redirect(url_for('auth.signup'))

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        user_data = {
            'username': username,
            'email': email,
            'password': hashed_password
        }
        mongo.db.users.insert_one(user_data)

        flash('Account created successfully! Please login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('auth/signup.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out', 'info')
    return redirect(url_for('auth.login'))

# # ------------------------------------------------------------------------
# @auth_bp.route('/')
# def home():
#     # When user visits root, redirect to login page
#     return redirect(url_for('auth.login'))



