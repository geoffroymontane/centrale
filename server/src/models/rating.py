"""
Define the Type model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Rating(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The rating model """

    __tablename__ = "rating"

    film = db.Column(db.Film, primary_key= True)
    user = db.Column(db.User, primary_key= True)
    rating = db.Column(db.Integer, nullable=True)


    def __init__(self, user, film, rating):
        """ Rate a film """
        self.user = user
        self.film = film
        self.rating = rating
