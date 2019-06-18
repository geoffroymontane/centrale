"""
Define the REST verbs relative to the films
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import FilmRepository
from util import parse_params


class FilmResource(Resource):
    """ Verbs relative to the films """

    @staticmethod
    @swag_from("../swagger/film/GET.yml")
    def get(title, date, author):
        film = FilmRepository.get(title=title, date=date, author=author)
        return jsonify({"film": film.json})

    @staticmethod
    @swag_from("../swagger/film/POST.yml")
    def post(title, date, author):
        """ Create a film based on the sent information """
        film = FilmRepository.create(
            title=title, date=date, author=author
        )
        return jsonify({"film": film.json})

    @staticmethod
    @parse_params(
        Argument("date", location="json", required=True, help="The date of the film.")
    )
    @swag_from("../swagger/film/PUT.yml")
    def put(title, date, author):
        """ Update a film based on the sent information """
        repository = FilmRepository()
        film = repository.update(title=title, date=date, author=author)
        return jsonify({"film": film.json})
