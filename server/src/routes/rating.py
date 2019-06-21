"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask_restful import Api

from resources import RatingResource

RATING_BLUEPRINT = Blueprint("rating", __name__)
Api(RATING_BLUEPRINT).add_resource(
    RatingResource, "/rating/<string:userfirstname>/<string:userlastname>/<string:filmtitle>/<string:filmauthor>"
)
