from flask import render_template, request, redirect, url_for, jsonify
# from models import UserType, Requests, Status, ServiceType
# from db import add_request, find_user_by_username, users_collection, requests_collection, get_your_helpers, \
#     get_requests_by_elder_user_id
from flask_login import login_required
from bson.objectid import ObjectId


def homepage():
    return render_template('homepage.html')

def welcome():
    return render_template('welcome.html')