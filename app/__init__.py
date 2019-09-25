import os

from flask import Flask, render_template, send_from_directory, json
from .views.mock import mock
from .views.index import index_blueprint
from .views.metrics import metrics


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, static_folder="build/static", template_folder="build")
    app.config.from_object('config')

    app.register_blueprint(mock)
    app.register_blueprint(index_blueprint)
    app.register_blueprint(metrics)

    return app
