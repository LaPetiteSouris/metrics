FROM python:3.5
MAINTAINER Tung Hoang


ENV INSTALL_PATH /skynet

RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY . .

WORKDIR  "/skynet"

RUN pip install -r requirements.txt

CMD gunicorn -b 0.0.0.0:3000 --access-logfile - "api.wsgi:app"
