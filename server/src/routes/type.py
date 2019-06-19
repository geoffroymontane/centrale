"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask_restful import Api

from resources import TypeResource
from resources import TypesResource

TYPES_BLUEPRINT = Blueprint("types", __name__)
Api(TYPES_BLUEPRINT).add_resource(
    TypesResource, "/types"
)

TYPE_BLUEPRINT = Blueprint("type", __name__)
Api(TYPE_BLUEPRINT).add_resource(
    TypeResource, "/type/<string:typename>"
)
