from data import db_session
from data.users import User
from flask import Flask, render_template, redirect
from forms.user_forms import RegisterForm, LoginForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user


app = Flask(__name__)
app.config["SECRET_KEY"] = "random_key_change_later"
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


def main():
    db_session.global_init("db/user_data.db")
    app.run(host="127.0.0.1", port=8080)


@app.route("/")
def index():
    return render_template("index.html", title="ShareMyTrip")


@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.login == form.login.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html', title="Авторизация",
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template("login.html", title="Авторизация", form=form)


@app.route("/signup", methods=["POST", "GET"])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.repeat.data:
            return render_template("signup.html", title='Регистрация',
                                   message="Пароли не совпадают", form=form)
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.login == form.login.data).first():
            return render_template("signup.html", title="Регистрация",
                                   message="Такой пользователь существует",
                                   form=form)
        user = User(login=form.login.data)
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect("/login")
    return render_template("signup.html", title="Регистрация", form=form)


@app.route("/confirm_logout")
def confirm_logout():
    return render_template("confirm_logout.html", title="Выход")


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


if __name__ == "__main__":
    main()