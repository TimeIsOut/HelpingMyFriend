from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class AddNewRouteForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    time_hours = StringField()
    budget = StringField()
    remarks = StringField()
    coordinates = TextAreaField(validators=[DataRequired()])
    submit = SubmitField('Сохранить')


