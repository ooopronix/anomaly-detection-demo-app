from flask import Blueprint

metrics = Blueprint('metrics', __name__, url_prefix='/metrics')


@metrics.route("/")
def metrics_endpoint():
    return "Hi, I'm a metric"

