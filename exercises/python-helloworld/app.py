from flask import Flask, json
import logging


app = Flask(__name__)

#setup logging basics including logfile and default level

logging.basicConfig(filename='app.log', level=logging.DEBUG)

health = {
    'result': 'OK - healthy'
}

usage = {
    'data': {'UserCount': 140, 'UserCountActive': 23}
}

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status", methods=['GET'])
def healthstatus():
    response = app.response_class(
        response=json.dumps(health),
        status=200,
        mimetype='application/json')

    return response

@app.route("/metrics", methods=['GET'])
def useage():
    response = app.response_class(
        response = json.dumps(usage),
        status = 200,
        mimetype = 'application/json')

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
