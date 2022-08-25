from flask import Flask
from flask import json
from flask.logging import create_logger
import logging

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

@app.route('/status')
def healthcheck():
    response = app.response_class(
        response=json.dumps({"result":"OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Status request successfull')
    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
        response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
        status=200,
        mimetype='application/json'
    )

    LOG.info(f"Metrics request successfull")
    return response

@app.route("/")
def hello():
    LOG.info(f"Main request successfull")

    return "Hello World v1.0.0!"

if __name__ == "__main__":
    ## stream logs to a file
    logging.basicConfig(filename='app.log',level=logging.DEBUG)

    app.run(host='0.0.0.0')