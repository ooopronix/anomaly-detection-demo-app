import os

from flask import Flask, render_template, send_from_directory, json


def create_app(test_config=None):
    # create and configure the app
    # app = Flask(__name__, instance_relative_config=True)
    app = Flask(__name__, static_folder="build/static", template_folder="build")

    app.config.from_object('config')
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/")
    def main():
        return render_template('index.html')

    @app.route("/mock/orderService")
    def order():
        data = {
            "products": [
                {
                    "id": "79161a98-30e0-11e7-b4e8-9801a798fc8f",
                    "pname": "bananas",
                    "pprice": 5.00,
                    "ptype": "fruit",
                    "image": "bananas.jpg",
                    "pquant": 1
                },
                {
                    "id": "7915f0cc-30e0-11e7-91c7-9801a798fc8f",
                    "image": "onions.jpg",
                    "pname": "onions",
                    "pprice": 3.00,
                    "ptype": "vegetables",
                    "pquant": 1
                },
                {
                    "id": "79169ffe-30e0-11e7-bf3b-9801a798fc8f",
                    "image": "milk.jpg",
                    "pname": "milk",
                    "pprice": 4.00,
                    "ptype": "dairy",
                    "pquant": 1
                },
                {
                    "id": "7916d9ba-30e0-11e7-b66f-9801a798fc8f",
                    "image": "cheese.jpg",
                    "pname": "cheese",
                    "pprice": 3.00,
                    "ptype": "dairy",
                    "pquant": 3
                },
                {
                    "id": "79165436-30e0-11e7-b79a-9801a798fc8f",
                    "image": "almonds.jpg",
                    "pname": "almonds",
                    "pprice": 10.00,
                    "ptype": "nuts",
                    "pquant": 1
                }
            ]
        }
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response

    # TODO: A proper fix for css/ico structuring to automatically serve them from satic_folder
    # TODO: Directly importing css into the jsx code will eliminate this issue
    @app.route('/favicon.ico')
    def send_ico():
        return send_from_directory(app.root_path + '/build/', 'favicon.ico', conditional=True)

    @app.route('/logo.svg')
    def send_logo():
        return send_from_directory(app.root_path + '/build/', 'logo.svg', conditional=True)

    @app.route("/css/<filename>")
    def send_css(filename):
        return send_from_directory(app.root_path + '/build/', "css/" + filename, conditional=True)

    @app.route("/images/<filename>")
    def send_images(filename):
        return send_from_directory(app.root_path + '/build/', "images/" + filename, conditional=True)

    return app
