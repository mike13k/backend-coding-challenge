from flask_restplus import Api
from flask import Blueprint


blueprint = Blueprint('api', __name__)

api = Api(blueprint)
