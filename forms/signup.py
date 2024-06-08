from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField



class RegisterForm(FlaskForm):
    name = StringField("Name", [validators.DataRequired()])
    username = StringField("Username", [validators.DataRequired()])
    password = PasswordField("Password", [validators.DataRequired()])
    submit = SubmitField("Register")