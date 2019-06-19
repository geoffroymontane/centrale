""" Defines the Type repository """

from models import Type

class TypeRepository:
    """ The repository for the user model """

    @staticmethod
    def getAll():
        """ Get all types """
        return Type.query.all()

    @staticmethod
    def create(typename):
        type_ = Type(typename = typename)
        return type_.save()
