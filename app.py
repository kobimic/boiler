from flask import Flask
from logger import logger
from db import session
from endpoints.routes import routes
from config import configuration
from error_handlers import register_error_handlers


def main():
    logger.info("Starting main...")
    app = Flask(configuration.name)
    app.register_blueprint(routes, url_prefix='/')
    register_error_handlers(app)
    app.run(debug=configuration.is_debug, host=configuration.host, port=configuration.port)


if __name__ == '__main__':
    main()
