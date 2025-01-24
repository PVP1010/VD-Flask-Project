# models.py: для определения моделей базы данных

from app import db, login_manager                                       # импорт объектов
from flask_login import UserMixin                                       # импорт класса UserMixin

@login_manager.user_loader                                              # маршрут для загрузки пользователя
def load_user(user_id):                                                 # функция загрузки пользователя
    return User.query.get(int(user_id))                                 # возвращает объект пользователя

class User(db.Model, UserMixin):                                        # класса для создания таблицы с базой данных User
    id = db.Column(db.Integer, primary_key=True)                        # первичный ключ
    username = db.Column(db.String(20), unique=True, nullable=False)    # поле username
    email = db.Column(db.String(120), unique=True, nullable=False)      # поле email
    password = db.Column(db.String(60), nullable=False)                 # поле password

    def __repr__(self):                                                 # метод __repr__
        return f'User: {self.username}, email: {self.email}'            # возвращает строку