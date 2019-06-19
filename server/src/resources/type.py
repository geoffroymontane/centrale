"""
Define the REST verbs relative to the types
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import TypeRepository
from util import parse_params


class TypesResource(Resource):
    """ Verbs relative to the types """

    @staticmethod
    @swag_from("../swagger/type/GET.yml")
    def get():
        """ Return all types """
        types = TypeRepository.getAll()
        _str = "["
        for i in range(len(types)):
                _str += types[i].typename + ","
        _str = _str[: len(_str) - 1] + "]"

        return _str

class TypeResource(Resource):
    @staticmethod
    @swag_from("../swagger/type/POST.yml")
    def post(typename):
        return jsonify({"type": TypeRepository.create(typename).json})
