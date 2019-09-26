import os

from flask import Flask, render_template, send_from_directory, json
from .views.mock import mock
from .views.index import index_blueprint
from prometheus_flask_exporter import PrometheusMetrics



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, static_folder="build/static", template_folder="build")

    app.config.from_object('config')

    app.register_blueprint(mock)
    app.register_blueprint(index_blueprint)

    # set up prometheus metrics exporting
    metrics = PrometheusMetrics(app)
    # static information as metric
    metrics.info('AnomalyDetectorDemo', 'Demo application for PAD/LAD', version='0.1')
    return app
