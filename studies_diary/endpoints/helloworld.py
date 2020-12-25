from studies_diary.restplus import api
from flask_restx import Resource

ns_default = api.default_namespace


# Exemplo de um hello word com get
@ns_default.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
