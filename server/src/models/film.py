"""
Define the Film model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Film(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Film model """

    __tablename__ = "film"

    title = db.Column(db.String(300), primary_key=True)
    author = db.Column(db.String(300), primary_key=True)
    date = db.Column(db.Integer())
    type = db.Column(db.String(300))
    image = db.Column(db.String(300))
    synopsis = db.Column(db.String(2000))
    country = db.Column(db.String(300))

    def __init__(self, title, author, date, type, image,synopsis,country):
        """ Create a new Film """
        self.title = title
        self.author = author
        self.date = date
        self.type = type
        self.image=image
        self.synopsis=synopsis
        self.country=country
