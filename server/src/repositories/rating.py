""" Defines the User repository """

from models import Rating


class RatingRepository:
    """ The repository for the rating model """

    @staticmethod
    def get(userfirstname, userlastname, filmtitle, filmauthor):
        """ Query a rating using user and film """
        return Rating.query.filter_by(userfirstname=userfirstname, userlastname=userlastname, filmtitle=filmtitle , filmauthor = filmauthor).one()

    def update(self, userfirstname, userlastname, filmtitle , filmauthor, newrating):
        """ Update a rating"""
        rating = self.get(userfirstname, userlastname, filmtitle ,filmauthor)
        rating.rating = newrating

        return rating.save()

    @staticmethod
    def create(userfirstname, userlastname, filmtitle, filmauthor, rating):
        """ Create a new rating """
        rating = Rating(userfirstname=userfirstname, userlastname=userlastname, filmtitle=filmtitle, filmauthor= filmauthor , rating=rating)

        return rating.save()
