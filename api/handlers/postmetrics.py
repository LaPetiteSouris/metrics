from influxdb import InfluxDBClient

from database import config
from utils import logger
from datetime import datetime

log = logger.define_logger('post metrics')
client = InfluxDBClient(config.INFLUX_HOST, config.INFLUX_PORT,
                        config.INFLUX_USER, config.INFLUX_PWD, config.INFLUX_DB
                        )


def on_metrics_post(req_body):
    req_body['time'] = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    client.write_points([req_body])
