import json
import os
import requests
import yaml
import sys

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from flask_swagger import swagger
from json import dumps


app = Flask(__name__)
api = Api(app)

dir_path = os.path.dirname(os.path.realpath(__file__))
with open("%s/geocoding-services.yml" % dir_path, 'r') as service_list:
    service_configuration = yaml.safe_load(service_list)
services = service_configuration['services']
for service_name in services.keys():
    print "loading " + service_name
    execfile('%s/services/%s.py' % (dir_path, service_name))


@app.route('/get_location')
@cross_origin()
def get_location():
    """
    Get Location

    Searching for latitude/longitude coordinates for the given location calling 3rd party APIs in order.
    Will return with the first valid result, or with empty array if none of the APIs were able to provide any results.
    ---
    parameters:
        - in: query
          name: search
    responses:
        200:
          description: Returns with Latitude & Longitude results
    """
    search_text = request.args.get('search')
    current_module = sys.modules[__name__]

    for service_name in services.keys():
        params = services[service_name]
        location_handler = getattr(current_module, "get_location_%s" % service_name)
        location = location_handler(search_text, params)
        if location is not None:
            location['search_text'] = search_text
            location['service_name'] = service_name
            return json.dumps(location)

    return json.dumps(None)


@app.route('/swagger.json')
@cross_origin()
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Geocode API"
    return jsonify(swag)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
