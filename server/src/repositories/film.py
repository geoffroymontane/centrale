""" Defines the Film repository """

from models import Film


class FilmRepository:
    """ The repository for the film model """

    @staticmethod
    def get(title, author):
        """ Query a film by title and date """
        return Film.query.filter_by(title=title, author=author).one()

    @staticmethod
    def getAll():
        """ Get all films """
        return Film.query.all()

    def update(self, title, author, date):
        """ Update a film's date"""
        film = self.get(title, author)
        film.date = date

        return film.save()

    @staticmethod
    def create(title, author, date):
        """ Create a new film """
        film = Film(title=title, author=author, date=date)
        return film.save()
