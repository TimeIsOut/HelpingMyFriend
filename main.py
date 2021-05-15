from data import db_session
from data.users import User
from data.routes import Route
from flask import Flask, render_template, redirect
from forms.user_forms import RegisterForm, LoginForm, ProfileButtons
from forms.route_forms import AddNewRouteForm
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


@login_required
@app.route("/profile", methods=["POST", "GET"])
def profile():
    form = ProfileButtons()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).get(current_user.id)
        if form.submit_change_login.data:
            user.login = form.new_login.data
            db_sess.commit()
            return render_template("profile.html", title="Профиль", form=form,
                                   message_login=True)
        elif form.submit_change_password.data:
            if not user.check_password(form.old_password.data):
                return render_template("profile.html", title="Профиль", form=form,
                                       message_password=[False, "Старый пароль неверен"])
            elif form.new_password.data != form.new_password_repeat.data:
                return render_template("profile.html", title="Профиль", form=form,
                                       message_password=[False, "Новые пароли не совпадают"])
            user.set_password(form.new_password.data)
            db_sess.commit()
            return render_template("profile.html", title="Профиль", form=form,
                                   message_password=[True, "Пароль успешно изменён"])
    return render_template("profile.html", title="Профиль", form=form)


@login_required
@app.route("/show_main")
def show_main():
    return render_template("show_map.html", title="Карта")


@login_required
@app.route("/all_routes")
def all_routes():
    db_sess = db_session.create_session()
    routes = db_sess.query(Route).all()
    users = db_sess.query(User).all()
    return render_template("all_routes.html", title="Все маршруты",
                           r=routes, u=users)


@login_required
@app.route("/my_routes/<int:id_author>")
def my_routes(id_author):
    db_sess = db_session.create_session()
    routes = db_sess.query(Route).filter(Route.author == id_author).all()
    return render_template("my_routes.html", title="Мои маршруты",
                           r=routes)


@login_required
@app.route("/route/<int:id>")
def route(id):
    db_sess = db_session.create_session()
    route = db_sess.query(Route).filter(Route.id == id).first()
    return render_template("route.html", title='Просмотр маршрута', r=route)


@login_required
@app.route("/add_new_route", methods=["POST", "GET"])
def add_route():
    form = AddNewRouteForm()
    if form.validate_on_submit():
        coords = form.coordinates.data.split("\r\n")
        time = form.time_hours.data if form.time_hours.data else None
        budget = form.budget.data if form.budget.data else None
        db_sess = db_session.create_session()
        route = Route(name=form.name.data,
                      coordinates=";".join(coords),
                      time_hours=time,
                      budget=budget,
                      remarks=form.remarks.data,
                      author=current_user.id)
        coords = [list(map(float, i.split(", "))) for i in coords]
        new_file = f"static/js/map_{route_id}.js"
        strings = open("static/js/map_template.js", "r").read().split("\n")
        strings.insert(6, f"        var coordinates = {coords}")
        with open(new_file, "a+") as file:
            file.write("\n".join(strings))
        db_sess.add(route)
        db_sess.commit()
        return redirect("/all_routes")
    return render_template("add_new_route.html", title='Добавление маршрута',
                           form=form)


@login_required
@app.route("/route/<int:id>/map")
def route_map(id):
    db_sess = db_session.create_session()
    route = db_sess.query(Route).filter(Route.id == id).first()
    return render_template("route_map.html", title="Карта", r=route)


@login_required
@app.route("/confirm_logout")
def confirm_logout():
    return render_template("confirm_logout.html", title="Выход")


@login_required
@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


if __name__ == "__main__":
    main()