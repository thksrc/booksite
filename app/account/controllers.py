from flask import Blueprint, render_template, request, redirect, session, url_for
from app import db
from app.models import User
from app.utils import set_password, check_password

account_bp = Blueprint("account", __name__)

@account_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if session.get('logged_in') is True:
            return redirect(url_for('main.home'), "303")
        else:
            return render_template("account/login.html", title="Login")
    elif request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        check_user = db.session.query(User).filter_by(username=username).first()
        if (username == ""):
            return render_template("account/login.html", title="Login", error="No Username")
        elif (password == ""):
            return render_template("account/login.html", title="Login", error="No Password")
        elif (check_user is None):
            return render_template("account/login.html", title="Login", error="Username DNE")
        elif not (check_password(check_user.password, password)):
            return render_template("account/login.html", title="Login", error="Wrong Password")
        else:
            session['logged_in'] = True
            user_db = User.query.filter_by(username=username).first()
            session['user_id'] = user_db.id
            session['username'] = user_db.username
            return redirect(url_for('main.home'))

@account_bp.route("/logout")
def logout():
    session['logged_in'] = False
    session['user_id'] = None
    session['username'] = None
    return redirect(url_for('main.home'))

@account_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        if session.get('logged_in') is True:
            return redirect(url_for('main.home'), "303")
        else:
            return render_template("account/register.html", title="Register")
    elif request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        confirm = request.form.get('confirm')

        password_hash = set_password(password)

        check_user = User.query.filter_by(username=username).first()
        if (username == ""):
            return render_template("account/register.html", title="Register", error="No Username")
        elif (password == ""):
            return render_template("account/register.html", title="Register", error="No Password")
        elif (confirm == ""):
            return render_template("account/register.html", title="Register", error="No Confirmation")
        elif (check_user is not None):
            return render_template("account/register.html", title="Register", error="Taken Username")
        elif (password != confirm):
            return render_template("account/register.html", title="Register", error="Different password")
        else:
            user = User(username=username,
                        password=password_hash)
            db.session.add(user)
            db.session.commit()
            session['logged_in'] = True
            user_db = User.query.filter_by(username=username).first()
            session['user_id'] = user_db.id
            session['username'] = user_db.username
            return redirect(url_for('main.home'))

@account_bp.route("/profile")
def profile():
    if session.get('logged_in') is True:
        user_data = {
            'username': session['username']
        }
        return render_template("account/profile.html", user_data=user_data, title="Profile")
    else:
        return redirect(url_for('main.home'))