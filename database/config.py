import os

INFLUX_HOST = os.getenv('INFLUX_HOST', 'localhost')
INFLUX_PORT = int(os.getenv('INFLUX_PORT', 8086))
INFLUX_USER = os.getenv('INFLUX_USER', 'telegraf')
INFLUX_DB = os.getenv('INFLUX_DB', 'telegraf')
INFLUX_PWD = os.getenv('INFLUX_PWD', 'telegraf')
