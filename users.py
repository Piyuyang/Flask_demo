from flask import Blueprint, current_app

users_bp = Blueprint("users", __name__)


@users_bp.route('/login')
def login():
    print(current_app.database)
    return "login page"
