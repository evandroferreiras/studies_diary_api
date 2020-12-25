""" Módulo app => inicialização da aplicação Flask
"""
from flask import Flask, Blueprint
from studies_diary.restplus import api
from studies_diary.endpoints.helloworld import ns_default
from studies_diary.endpoints.category import ns_category
from studies_diary.db import config_db
from studies_diary.log import log

app = Flask(__name__)


def initialize_app(app):
    # RESTPLUS_VALIDATE => True, habilita um comportamento de validação dos campos esperados em cada requisição
    app.config['RESTPLUS_VALIDATE'] = True
    # ERROR_404_HELP => False, desabilita uma mensagem de erro padrão
    app.config['ERROR_404_HELP'] = False

    config_db(app)
    # Flask Blueprint cria componentes para a aplicação. É como se fosse a “planta” de sua API.
    blueprint = Blueprint('api', __name__)
    api.init_app(blueprint)
    app.register_blueprint(blueprint)

    # RESTPlus (restx) utiliza o conceito de Resources e Namespaces.
    # Um Resource é basicamente a representação de algum endpoint da sua API.
    # E um Namespace é um conjunto de Resources.
    # Nesse exemplo, ambos são definidos no diretório /studies_diary/endpoints.
    # Para que a API reconheça a existência destes Namespaces,
    # é necessário adiciona-los utilizando a função api.add_Namespace()
    api.add_namespace(ns_default)
    api.add_namespace(ns_category)


def main():
    initialize_app(app)
    log.info(
        '>>>>> Starting development server at http://{}/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=True)


if __name__ == '__main__':
    main()
