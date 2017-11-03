from api import config
from api.server import app
from utils import logger

log = logger.define_logger('API started')

if __name__ == "__main__":
    log.info('service ready', extra={'server': {'host': config.HOST, 'port': config.PORT}})
    app.run(debug=False, host=config.HOST, port=config.PORT)
