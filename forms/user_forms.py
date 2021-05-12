from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    login = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    repeat = PasswordField(validators=[DataRequired()])
    submit = SubmitField("Зарегистрироваться")


class LoginForm(FlaskForm):
    login = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    remember_me = BooleanField("Запомнить меня")
    submit = SubmitField("Войти")


class ProfileButtons(FlaskForm):
    new_login = StringField()
    submit_change_login = SubmitField("Сохранить логин")
    old_password = PasswordField()
    new_password = PasswordField()
    new_password_repeat = PasswordField()
    submit_change_password = SubmitField("Сохранить пароль")