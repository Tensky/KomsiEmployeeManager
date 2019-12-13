from flask import Blueprint
from app import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return 'LOGIN'


@auth.route('/signup')
def signup():
    return 'SIGNUP'


@auth.route('/logout')
def logout():
    return 'LOGOUT'
