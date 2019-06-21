"""
Define the Type model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Rating(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The rating model """

    __tablename__ = "rating"

    filmtitle = db.Column(db.String, primary_key= True)
    filmauthor = db.Column(db.String, primary_key= True)
    userfirstname = db.Column(db.String, primary_key= True)
    userlastname = db.Column(db.String, primary_key= True)
    rating = db.Column(db.Integer, nullable=True)


    def __init__(self, userfirstname, userlastname, filmtitle, filmauthor, rating):
        """ Rate a film """
        self.filmtitle = filmtitle
        self.filmauthor = filmauthor
        self.userfirstname = userfirstname
        self.userlastname = userlastname
        self.rating = rating
