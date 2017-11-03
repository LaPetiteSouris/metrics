from flask import Blueprint, jsonify

from api.errors.api_exception import MetricPostFailure
from utils import logger

error_handler_api = Blueprint('error_handler_api', __name__)
log = logger.define_logger('error handler api')


@error_handler_api.app_errorhandler(MetricPostFailure)
def handle_not_implemented(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
