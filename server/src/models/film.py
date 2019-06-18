"""
Define the Film model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Film(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Film model """

    __tablename__ = "film"

    title = db.Column(db.String(300), primary_key=True)
    date = db.Column(db.Integer())
    author = db.Column(db.String(300), nullable=True)

    def __init__(self, title, date, author):
        """ Create a new Title """
        self.title = title
        self.date = date
        self.author = author
