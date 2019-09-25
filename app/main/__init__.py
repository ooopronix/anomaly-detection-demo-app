from flask import Blueprint

bp = Blueprint('main', __name__, template_folder='../web/build')

from app.main import routes
