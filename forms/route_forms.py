from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class AddNewRouteForm(FlaskForm):
    """
    Форма для добавления маршрута

    :param name: название маршрута
    :param time_hours: время маршрута
    :param budget: бюджет маршрута
    :param remarks: заметки для маршрута
    :param coordinates: координаты точек маршрута
    :param submit: сохранить форму(маршрут)
    """

    name = StringField(validators=[DataRequired()])
    time_hours = StringField()
    budget = StringField()
    remarks = StringField()
    coordinates = TextAreaField(validators=[DataRequired()])
    submit = SubmitField('Сохранить')


