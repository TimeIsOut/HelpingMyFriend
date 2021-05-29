from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    """
    Форма регистарции

    :param login: поле для логина
    :param password: поле для пароля
    :param repeat: поле для повторного ввода пароля
    :param submit: подтверждение регистрации

    """
    login = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    repeat = PasswordField(validators=[DataRequired()])
    submit = SubmitField("Зарегистрироваться")


class LoginForm(FlaskForm):
    """
    Форма логина

    :param login: поле для логина
    :param password: поле для пароля
    :param remember_me: запомнить пароль
    :param submit: подтверждение входа

    """
    login = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    remember_me = BooleanField("Запомнить меня")
    submit = SubmitField("Войти")


class ProfileButtons(FlaskForm):
    """
    Форма для изменения профиля

    :param new_login: поле для нового логина
    :param submit_change_login: подтверждение смены логина
    :param old_password: поле для подтверждения старого пароля
    :param new_password: поле для ввода нового пароля
    :param new_password_repeat: повторный ввод нового пароля
    :param submit_change_password: подтверждение смены пароля

    """
    new_login = StringField()
    submit_change_login = SubmitField("Сохранить логин")
    old_password = PasswordField()
    new_password = PasswordField()
    new_password_repeat = PasswordField()
    submit_change_password = SubmitField("Сохранить пароль")