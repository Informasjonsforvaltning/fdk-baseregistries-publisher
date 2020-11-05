"""Service layer module for fdk_baseregistries_publisher."""
from rdflib import Graph


def fetch_baseregistries() -> Graph:
    """Fetch a catalog of datasets representing base registries."""
    return Graph()
