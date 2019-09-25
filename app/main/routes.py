from flask import render_template

from app.main import bp
#from app.models.job import Job


@bp.route('/')
def index():
    """Main page route."""
    return render_template('index.html')

#
# @bp.route('/add_job')
# def add_job():
#     """Adds job4 to the database."""
#     new_job = Job(name='job4')
#     new_job.insert()
#     return '', 204
