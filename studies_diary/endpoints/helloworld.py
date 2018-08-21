from studies_diary.restplus import api
from flask_restplus import Resource

ns = api.default_namespace


@ns.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
