from studies_diary.restplus import api
from flask_restplus import Resource

ns_default = api.default_namespace


@ns_default.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
