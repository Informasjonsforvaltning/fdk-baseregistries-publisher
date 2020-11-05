"""Resource module for ready."""
from typing import Any

from flask import Response
from flask_restful import Resource


class Ready(Resource):
    """Class representing ready resource."""

    @staticmethod
    def get() -> Any:
        """Ready route function."""
        return Response("OK")
