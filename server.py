from flask import Flask, render_template, send_from_directory, json
app = Flask(__name__, static_folder="build/static", template_folder="build")


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/mock/orderService")
def order():
    data = {"table": [
        {
            "id": "1",
            "pname": "bananas",
            "pprice": 5,
            "ptype": "fruit",
            "image": "bananas.jpg",
            "pquant": 1
        },
        {
            "id": "2",
            "image": "onions.jpg",
            "pname": "onions",
            "pprice": 3,
            "ptype": "vegetables",
            "pquant": 1
        },
        {
            "id": "3",
            "image": "milk.jpg",
            "pname": "milk",
            "pprice": 4,
            "ptype": "dairy",
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
def sendIco():
    return send_from_directory(app.root_path + '/build/', 'favicon.ico', conditional=True)

@app.route('/logo.svg')
def sendLogo():
    return send_from_directory(app.root_path + '/build/', 'logo.svg', conditional=True)


@app.route("/css/patternfly-additions.css")
def sendPF():
    return send_from_directory(app.root_path + '/build/', "css/patternfly-additions.css", conditional=True)


@app.route("/css/react-bootstrap-table.css")
def sendBS():
    return send_from_directory(app.root_path + '/build/', "css/patternfly-additions.css", conditional=True)


@app.route("/css/main.css")
def sendMainCSS():
    return send_from_directory(app.root_path + '/build/', "css/main.css", conditional=True)


app.debug=True
app.run(host='0.0.0.0')
