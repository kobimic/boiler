from werkzeug.exceptions import NotFound
from logger import logger
from exceptions.exceptions import ValidationException, PageNotFound
from flask import jsonify, Flask


def error_handler_404(error):
    body = {'error_description': 'page not found'}
    return jsonify(body), 404


def error_handler_validation(error):
    body = {'error_description': str(error)}
    return jsonify(body), 500


def error_handler_exception(error):
    body = {'error_description': str(error)}
    logger.error(body)
    return jsonify(body), 500


def register_error_handlers(app:Flask):
    # these are exception handlers
    app.register_error_handler(NotFound, error_handler_404)
    app.register_error_handler(ValidationException, error_handler_validation)
    app.register_error_handler(Exception, error_handler_exception)