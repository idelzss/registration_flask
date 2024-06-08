from .base import Base
from sqlalchemy import Column, Integer, String
from flask_login import UserMixin
from werkzeug.security import check_password_hash
class User(Base, UserMixin):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(40), unique=True)
    password = Column(String(16))
    name = Column(String(50))

    def __init__(self, username: str, password: str, name: str):
        self.username = username
        self.password = password
        self.name = name

    def __str__(self):
        return f'User: {self.id}: {self.username}'

    def check_password(self, password):
        return check_password_hash(self.password, password)