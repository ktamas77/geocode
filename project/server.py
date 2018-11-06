from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
import requests
import json
import yaml
import os
import sys

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
def get_location():
    search_text = request.args.get('search')

    for service_name in services.keys():
        params = services[service_name]
        location_handler = getattr(sys.modules[__name__], "get_location_%s" % service_name)
        location = location_handler(search_text, params)
        if location is not None:
            location['search_text'] = search_text
            location['service_name'] = service_name
            return json.dumps(location)

    return json.dumps(None)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
