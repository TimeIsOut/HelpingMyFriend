import sqlalchemy
from .db_session import SqlAlchemyBase


class Route(SqlAlchemyBase):
    __tablename__ = 'routes'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                                               autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    coordinates = sqlalchemy.Column(sqlalchemy.String)
    time_hours = sqlalchemy.Column(sqlalchemy.Float)
    budget = sqlalchemy.Column(sqlalchemy.Float)
    remarks = sqlalchemy.Column(sqlalchemy.String)
    author = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'))

