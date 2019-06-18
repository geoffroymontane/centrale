"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask_restful import Api

from resources import FilmResource

FILM_BLUEPRINT = Blueprint("film", __name__)
Api(FILM_BLUEPRINT).add_resource(
    FilmResource, "/film/<string:title>/<int:date>/<string:author>"
)
