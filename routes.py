from . import app, login_manager
from flask import render_template, redirect, flash
from .forms import LoginForm, RegisterForm
from .database import User, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/signup", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        username = form.username.data

        # user = session.query(User).where(User.username == username)
        # if user:
        #     flash("User exists. Please, try to login or try other username or password")
        #     return redirect("/login")

        new_user = User(
            username=username,
            password=generate_password_hash(password),
            name=name
        )

        try:
            session.add(new_user)
            session.commit()
            flash("registration successful!")
            return redirect("/")
        except Exception as exc:
            return f"{exc}"
        finally:
            session.close()
    else:
        return render_template("signup.html", form=form)
#Перевіряє чи є юзер в базі і редіректить на логін



@app.route("/login", methods=["GET", "POST"])
def log_in():
    form = LoginForm()
    if form.validate_on_submit():
        password = form.password.data
        username = form.username.data

        user = session.query(User).where(User.username == username).first()
        if user:
            login_user(user)
            flash("Login successful!")
            return redirect("/")
        else:
            flash("Wrong password or username. Please, check")
            return redirect("/login")
    else:
        return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/login")

@login_manager.user_loader
def user_loader(user_id):
    return session.query(User).get(int(user_id))
