from flask import Blueprint, render_template, request, flash, redirect, session

from app import db
from models import UserModel

auth = Blueprint('auth', __name__)


@auth.route('/login')
def loginpage():
    return render_template("login.html")


@auth.route('/login', methods=["POST"])
def login():
    email = request.form['email']
    password = request.form['password']
    if db.session.query(UserModel).filter(UserModel.email == email).count() == 0:
        flash("Anda Ngigau. Nda ada email seperti itu di database kami")
        return render_template("login.html")
    elif db.session.query(UserModel).filter(UserModel.email == email and UserModel.password == password).count() != 0:
        session['email'] = email
        session['loged_in'] = True
        return redirect("/")
    else:
        flash("Password salah gan. email udah bener")
        return render_template("login.html")


@auth.route('/signup')
def signuppage():
    return render_template('signup.html')


@auth.route('/signup', methods=["POST"])
def signup():
    email = request.form['email']
    name = request.form['name']
    password = request.form['password']
    if db.session.query(UserModel).filter(UserModel.email == email).count() != 0:
        flash("Email sudah pernah digunakan")
        return render_template("login.html")
    else:
        user = UserModel(name, email, password)
        db.session.add(user)
        db.session.commit()
        return redirect('/')


@auth.route('/logout')
def logout():
    return 'LOGOUT'
