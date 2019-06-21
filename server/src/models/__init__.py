from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .film import Film
from .type import Type
from .rating import Rating
