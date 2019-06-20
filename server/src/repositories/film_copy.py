""" Defines the Film repository """

from models import Film


class FilmRepository:
    """ The repository for the film model """

    @staticmethod
    def get(title, date, author):
        """ Query a film by title and date and author """
        return Film.query.filter_by(title=title).one()

    @staticmethod
    def create(title, date, author):
        """ Create a new film """
        film = Film(title=title, date=date, author=author)
        return film.save()
