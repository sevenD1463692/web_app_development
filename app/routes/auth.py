from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.user import User

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET'])
def login():
    """
    Display the login form.
    """
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template('auth/login.html')

@auth_bp.route('/login', methods=['POST'])
def login_post():
    """
    Handle user login authentication.
    """
    username = request.form.get('username')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(username=username).first()

    if not user or not user.check_password(password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('index'))

@auth_bp.route('/register', methods=['GET'])
def register():
    """
    Display the registration form.
    """
    return render_template('auth/register.html')

@auth_bp.route('/register', methods=['POST'])
def register_post():
    """
    Handle user registration.
    """
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.register'))

    user = User.query.filter_by(username=username).first()
    if user:
        flash('Username already exists')
        return redirect(url_for('auth.register'))

    new_user = User.create(username=username, email=email, password=password)
    
    if new_user:
        flash('Registration successful! Please log in.')
        return redirect(url_for('auth.login'))
    else:
        flash('An error occurred during registration. Please try again.')
        return redirect(url_for('auth.register'))

@auth_bp.route('/logout')
@login_required
def logout():
    """
    Log out the current user.
    """
    logout_user()
    return redirect(url_for('auth.login'))
