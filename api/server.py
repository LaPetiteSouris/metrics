from flask import Flask

from api import config
from api.errors.error_handler import error_handler_api
from api.routes import metrics_api
from utils import logger

log = logger.define_logger('API started')

app = Flask(__name__)
app.register_blueprint(metrics_api)
app.register_blueprint(error_handler_api)


if __name__ == "__main__":
    log.info('service ready', extra={'server': {'host': config.HOST, 'port': config.PORT}})
    app.run(debug=False, host=config.HOST, port=config.PORT)
