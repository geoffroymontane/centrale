"""
Define the REST verbs relative to the users
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import RatingRepository
from util import parse_params


class RatingResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    @swag_from("../swagger/rating/GET.yml")
    def get(userfirstname, userlastname, filmtitle, filmauthor):
        """ Return a rate """
        rating = RatingRepository.get(userfirstname=userfirstname, userlastname=userlastname, filmtitle=filmtitle, filmauthor= filmauthor)
        return jsonify({"rating": rating.json})

    @staticmethod
    @parse_params(
        Argument("rating", location="json", required=True, help="The rate of the user for the film.")
    )
    @swag_from("../swagger/rating/POST.yml")
    def post(userfirstname, userlastname, filmtitle, filmauthor, rating):
        """ Create a rate """
        rating = RatingRepository.create(
            userfirstname=userfirstname, userlastname=userlastname , filmtitle=filmtitle, filmauthor=filmauthor , rating=rating
        )
        return jsonify({"rating": rating.json})

    @staticmethod
    @parse_params(
        Argument("rating", location="json", required=True, help="The rate of the user for this film.")
    )
    @swag_from("../swagger/rating/PUT.yml")
    def put(userfirstname, userlastname , filmtitle, filmauthor , rating):
        """ Update a rate"""
        repository = RatingRepository()
        rating = repository.update(userfirstname=userfirstname, userlastname=userlastname, filmtitle=filmtitle, filmauthor=filmauthor , rating= rating)
        return jsonify({"rating": rating.json})
