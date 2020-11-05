"""Resource module for ready."""
from flask import Response
from flask_restful import Resource

from fdk_baseregistries_publisher.service import (
    fetch_baseregistries,
)


class Baseregistries(Resource):
    """Class representing baseregistries resource."""

    def get(self) -> Response:
        """Get all catalogs."""
        registries = fetch_baseregistries()
        return Response(
            registries.serialize(format="text/turtle", encoding="utf-8"),
            mimetype="text/turtle",
        )
