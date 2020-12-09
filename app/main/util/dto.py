from flask_restplus import Namespace


class LangDto:
    api = Namespace('Trending Languages',
            description='List the languages used by the 100 trending public repos on GitHub,\
                 including repo count, and repos(repos name, url, owner, stars count).')