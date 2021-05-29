import sqlalchemy
from .db_session import SqlAlchemyBase


class Route(SqlAlchemyBase):
    """
    Класс описания маршрута

    :param name: название маршрута
    :param coordinates: координаты точек маршрута
    :param time_hours: время маршрута
    :param budget: бюджет маршрута
    :param remarks: заметки для маршрута
    :param author: автор маршрута

    """
    __tablename__ = 'routes'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                                               autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    coordinates = sqlalchemy.Column(sqlalchemy.String)
    time_hours = sqlalchemy.Column(sqlalchemy.Float)
    budget = sqlalchemy.Column(sqlalchemy.Float)
    remarks = sqlalchemy.Column(sqlalchemy.String)
    author = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))



