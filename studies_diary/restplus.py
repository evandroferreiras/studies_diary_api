import traceback
from studies_diary.log import log
from flask_restx import Api
from sqlalchemy.orm.exc import NoResultFound

descricao = 'Uma demonstração de uma api RestFul com Flask. <br> O projeto RestPlus foi substituído por RestX '
descricao += 'https://github.com/python-restx/flask-restx'
api = Api(version='1.0', title='API Estudos Diários',
          description=descricao)


@api.errorhandler
def default_error_handler(e):
    message = 'Uma exceção ocorreu.'
    log.exception(message)
    return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    log.warning(traceback.format_exc())
    return {'message': 'Um item do banco de dados foi solicitado, mas nenhum foi encontrado'}, 404
