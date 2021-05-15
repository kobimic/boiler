from flask import Flask, app, request
from logger import logger
from db import session
from endpoints.routes import routes
from config import configuration
from error_handlers import register_error_handlers

app = Flask(configuration.name)


@app.before_request
def before_request_func():
    logger.debug(f"before request: url path {request.path}")


@app.after_request
def after_request_func(response):
    logger.debug(f"after request: {response}")
    return response


def main():
    logger.info("Starting main...")
    app.register_blueprint(routes, url_prefix='/')
    register_error_handlers(app)
    app.run(debug=configuration.is_debug, host=configuration.host, port=configuration.port)


if __name__ == '__main__':
    main()
