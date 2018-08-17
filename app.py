import logging
from flask import Flask, Blueprint
from api.restplus import api
from api.endpoints.helloworld import HelloWorld

app = Flask(__name__)


def initialize_log():
    handler = logging.FileHandler("study-api.log")
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.INFO)
    log.addHandler(handler)

    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)
    log.addHandler(handler)
    return log


log = initialize_log()


def initialize_app(app):
    blueprint = Blueprint('api', __name__)
    api.init_app(blueprint)
    api.add_resource(HelloWorld)
    app.register_blueprint(blueprint)


def main():
    initialize_app(app)
    log.info(
        '>>>>> Starting development server at http://{}/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=True)


if __name__ == '__main__':
    main()
