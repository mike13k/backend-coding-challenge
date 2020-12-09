from flask_restplus import Api
from flask import Blueprint

from .main.controller.lang_controller import api as lang_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint)

api.add_namespace(lang_ns, path='/lang')