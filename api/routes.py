from flask import Blueprint, g, jsonify, request

from api.errors.api_exception import MetricPostFailure
from api.handlers.postmetrics import on_metrics_post
from utils import logger

metrics_api = Blueprint('metrics', __name__)
log = logger.define_logger('metrics API api')


@metrics_api.after_request
def per_request_callbacks(response):
    for func in getattr(g, 'call_after_request', ()):
        response = func(response)
    return response


@metrics_api.route('/ping', methods=['GET'])
def index():
    return jsonify({'response': 'pong'}), 200


@metrics_api.route('/metrics', methods=['POST'])
def sendmetrics():
    try:
        on_metrics_post(request.json)
    except Exception as e:
        log.warning('error posting metrics',
                    extra={'endpoint': '/metrics', 'method': request.method,
                           'request': str(request.json)})
        raise MetricPostFailure(
            'Metric post failure:{}'.format(str(e)), status_code=501)

    log.info('receving metrics post',
             extra={'endpoint': '/metrics', 'method': request.method,
                    'request': str(request.json)})

    return jsonify({'received': True}), 200
