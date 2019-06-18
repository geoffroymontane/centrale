"""
Define the Type model
"""
from . import db
from .abc import BaseModel, MetaBaseModel


class Type(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The type model """

    __tablename__ = "type"

    typename = db.Column(db.String(300), primary_key=True)

    def __init__(self, typename):
        """ Create a new Type """
        self.typename = typename
