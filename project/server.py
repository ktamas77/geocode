from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)


@app.route('/get_location')
def get_location():
    return "hello"


@app.route('/')
def hello():
    return "hey"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')
