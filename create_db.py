# Скрипт для создания базы данных.

from app import db
from app.models import User

db.create_all()
