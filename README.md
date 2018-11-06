# geocode
Geocoding Service

### Quick Start
Before start, please configure the services you'd like to use in the `services/geocoding-services.yml` file by
adding your api keys.

The application runs in docker, to start, type:
`./start.sh`

The service will listen to all connections on localhost at standard port 80.
Swagger will also start at localhost at port 8080 for testing.

### Endpoints
There is one endpoint:

`GET /get_location?search=<address>`

Example:

http://localhost/get_location?search=Sidney

### Services as Plugins
The geocoding service can be dynamically extended with plugins.
Plugins are automatically loaded at start.

#### The Service List Configuration
Available services are listed in the `services/geocoding-services.yml` yaml file.
The order of the services in this file determines the order of calls.
Arbitrary parameters (such as usernames, password, api keys) can be passed to each service as needed.

#### The Service Plugins
Services listed in the service list configuration file can be implemented in the `services` directory.
For an example if you called a service `hello` in the config file, the filename should be `services/hello.py`.
Then in the file one function needs to be created, in `get_location_<service_name>` format.
The implementation should return with a dictionary with the `Longitude` and `Latitude` parameters or with `None` if the service couldn't be executed.

### Swagger
Swagger documentation and a Swagger Docker Service added to the Geocoding service, so you can try it in your browser.
You can access Swagger here:
`http://localhost:8080`

### Questions?
Tamas Kalman <ktamas77@gmail.com>