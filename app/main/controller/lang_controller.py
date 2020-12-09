from flask_restplus import Resource

from ..util.dto import LangDto
from ..service import lang_service


api = LangDto.api


# List the languages used by the 100 trending public repos on GitHub, including language rank, repo count, and repos(repos name, url, owner, stars count).
@api.route('/')
class LangList(Resource):
    @api.doc('List the languages used by the 100 trending public repos on GitHub, including repo count, and repos(repos name, url, owner, stars count).')
    def get(self):
        return lang_service.trending_repo_languages()
