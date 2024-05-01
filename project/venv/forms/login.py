from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    with open('project/venv/static/very_impotent.txt', 'r') as file:
        var = file.read().split()
        email = EmailField(var[0], validators=[DataRequired()])
        password = PasswordField(var[1], validators=[DataRequired()])
        remember_me = BooleanField(var[2])
        submit = SubmitField(var[3])
