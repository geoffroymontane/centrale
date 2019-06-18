"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask_restful import Api

from resources import FilmResource
from resources import FilmsResource

FILM_BLUEPRINT = Blueprint("film", __name__)
Api(FILM_BLUEPRINT).add_resource(
    FilmResource, "/film/<string:title>/<string:author>"

)

FILMS_BLUEPRINT = Blueprint("films", __name__)
Api(FILMS_BLUEPRINT).add_resource(
    FilmsResource, "/films"
)
