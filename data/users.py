import sqlalchemy
from .db_session import SqlAlchemyBase
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    """
    Класс пользователя

    :param id: id пользователя
    :param login: логин пользователя
    :param hashed_password: закодированный хеш-пароль

    """
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False,
                                               primary_key=True,
                                               autoincrement=True)
    login = sqlalchemy.Column(sqlalchemy.String)
    hashed_password = sqlalchemy.Column(sqlalchemy.String)

    def set_password(self, password):
        """
        Генерация хеша
        """
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        """
        Проверка хеша пароля
        """
        return check_password_hash(self.hashed_password, password)