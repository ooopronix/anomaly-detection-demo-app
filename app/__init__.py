import os

from flask import Flask, render_template, send_from_directory, json
from .views.mock import mock
from .views.index import index_blueprint
from prometheus_flask_exporter import PrometheusMetrics
from flask.logging import default_handler
from logging.handlers import RotatingFileHandler
import logging


def create_app(test_config=None):

    # create and configure the app
    app = Flask(__name__, static_folder="build/static", template_folder="build")

    dir_name = 'logs'
    try:
        # Create log Directory
        os.mkdir(dir_name)
        print("Directory ", dir_name, " Created ")
    except FileExistsError:
        print("Directory ", dir_name, " already exists")

    # app.logger.removeHandler(default_handler)
    handler = RotatingFileHandler('logs/orders.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)

    app.config.from_object('config')

    app.register_blueprint(mock)
    app.register_blueprint(index_blueprint)

    # set up prometheus metrics exporting
    metrics = PrometheusMetrics(app)
    # static information as metric
    metrics.info('AnomalyDetectorDemo', 'Demo application for PAD/LAD', version='0.1')
    return app
