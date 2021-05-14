from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class AddNewRouteForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    time_hours = StringField()
    budget = StringField()
    remarks = StringField()
    coordinates = StringField(validators=[DataRequired()])
    submit = SubmitField('Сохранить')


