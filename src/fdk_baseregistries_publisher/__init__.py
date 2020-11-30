"""Package for exposing base registry descriptions in a Flask API."""
import json
from typing import Any

from dotenv import load_dotenv
from flask import Flask, make_response, Response
from flask_restful import Api

from .exceptions.exeption import FetchFromServiceException
from .resources.baseregistries import Baseregistries
from .resources.ping import Ping
from .resources.ready import Ready


__version__ = "0.1.0"


def create_app(test_config: Any = None) -> Flask:
    """Create and configure the app."""
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # Get environment
    load_dotenv()

    api = Api(app)

    # healthcheck routes
    api.add_resource(Ping, "/ping")
    api.add_resource(Ready, "/ready")

    api.add_resource(Baseregistries, "/baseregistries")

    @app.errorhandler(FetchFromServiceException)
    def handle_sparql_wrapper_exceptions(e: FetchFromServiceException) -> Response:
        # replace the body with JSON
        response = make_response()
        response.data = json.dumps({"message": e.message})
        response.content_type = "application/json"
        response.status_code = e.status
        return response

    return app
