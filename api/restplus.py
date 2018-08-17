from flask_restplus import Api
import logging

log = logging.getLogger(__name__)

api = Api(version='1.0', title='Study Diary API',
          description='A demonstration of Flask RestPlus')

@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)
    return {'message': message}, 500
