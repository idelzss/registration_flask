from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField



class LoginForm(FlaskForm):
    username = StringField("Username", [validators.DataRequired()])
    password = PasswordField("Password", [validators.DataRequired()])
    submit = SubmitField("Log in")

#validators - робить обов'язковим до заповнення