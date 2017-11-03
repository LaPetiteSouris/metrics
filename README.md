### Skynet

**Be aware, we are watching you**

This is a demo project to utilize the power of time-series database and visualization tool to easily build a tracking system to monitor your product and clients' activities. Thanks to Grafana, we have the possibility to easily build customized business dashboard in matter of minutes.

**How does it work ?**

The API accept JSON-formated metrics from any clients and register the data into InfluxDB. Thanks to Grafana, we can easily build and monitor dashboard from InfluxDB data in real-time.

The simply API with bullet-proof design is able to handle massive amount of requests, suitable for tracking product with high interaction levels (web, mobile...etc)

**How to try ?**

1. Make sure that you have InfluxDB and Grafana set up correctly. You may use
a ready made docker image which contains both service out-of-the-box

2. Build the app with Docker, else you are a fan of `pyenv` or `virtualenv`,
just create one new environment and do `pip install -r requirements.txt`. If you are using
this method, you have to launch `python api/server.py`. You may need to add current `DIR` to
`PYTHONPATH`
