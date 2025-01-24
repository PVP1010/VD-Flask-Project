# основной файл для инициализации пакета

from flask import Flask                                    # импорт класса Flask
from flask_sqlalchemy import SQLAlchemy                    # импорт класса SQLAlchemy
from flask_bcrypt import Bcrypt                            # импорт класса Bcrypt
from flask_login import LoginManager                       # импорт класса LoginManager


app = Flask(__name__)                                       # объект класса Flask
app.config['SECRET_KEY'] = 'your_secret_key'                # секретный ключ
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' # база данных

db = SQLAlchemy(app)                                        # объект класса SQLAlchemy
bcrypt = Bcrypt(app)                                        # объект класса Bcrypt
login_manager = LoginManager(app)                           # объект класса LoginManager
login_manager.login_view = 'login'                          # маршрут для страницы входа

from app import routes                                      # импорт модуля