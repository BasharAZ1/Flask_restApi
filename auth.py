from db import add_user, find_user_by_username, check_user_password, users_collection, user_from_dict
from flask_login import login_user, logout_user, login_required
from flask import render_template, request, redirect, flash, session, url_for,jsonify,abort
from models import  User


@login_required
def logout():
    session.clear()
    logout_user()
    return redirect(url_for('homepage'))


def login():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user_dict = find_user_by_username(username)
        if user_dict and check_user_password(username, password):
            user = user_from_dict(user_dict)

            session['username'] = user.username
            session['phone'] = user.phone
            session['user_id'] = str(user._id)
            session['is_logged_in'] = True
            login_user(user)

            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"error": "Invalid username or password"}), 401

    return render_template('login.html')

def is_password_legal(password):
    if len(password) < 8:
        return False
    special_characters = "!@#&%()"
    if not any(char in special_characters for char in password):
        return False

    return True

def register():
    if request.method == 'GET':
        return render_template('signup.html')
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        username = data.get('username')
        phone_prefix = data.get('phone_prefix')
        email = data.get('email')
        phone = data.get('phone')
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        full_phone_number = '972' + phone_prefix[1:] + phone

        if password != confirm_password:
            return jsonify({"error": "Passwords do not match!"}), 400

        existing_user = users_collection.find_one({"$or": [{"username": username}, {"phone": phone}]})
        if existing_user:
            return jsonify({"error": "Username or phone number already taken. Please choose another."}), 400

        new_user = User(username=username, phone=full_phone_number, password=password, email=email)
        add_user(new_user)

        return jsonify({"message": "User registered successfully"}), 201
    return jsonify({"error": "Method not allowed"}), 405