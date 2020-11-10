"""Service layer module for fdk_baseregistries_publisher."""
from os import environ as env

from rdflib import Graph, Namespace, RDF, URIRef

from .exceptions.exeption import FetchFromServiceException


BASEREGISTRY_CATALOG_URL = env.get(
    "BASEREGISTRY_CATALOG_URL",
    "https://baseregistries-publisher.fellesdatakatalog.digdir.no",
)

DCAT = Namespace("http://www.w3.org/ns/dcat#")

BASEREGISTRY_DATASET_URLS = [
    "https://datasets.fellesdatakatalog.digdir.no/datasets/68d08f28-a16d-4fab-a953-ed4ab08ce2e2"
]

catalog = Graph()
baseregister_catalog = URIRef(BASEREGISTRY_CATALOG_URL)


def fetch_baseregistries() -> Graph:
    """Fetch a catalog of datasets representing base registries."""
    _catalog = _create_catalog_graph()
    _registries = Graph()

    for url in BASEREGISTRY_DATASET_URLS:
        _registries += _get_dataset_by_url(url)
        # Get the node for the dataset:
        _baseregistry = _registries.value(
            predicate=RDF.type, object=DCAT.Dataset, any=False
        )
        # Add the node to the catalog:
        _catalog.add((baseregister_catalog, DCAT.dataset, _baseregistry))
    catalog = _catalog + _registries
    return catalog


def _create_catalog_graph() -> Graph:
    _g = Graph()

    _g.bind("dcat", DCAT)
    _g.add((baseregister_catalog, RDF.type, DCAT.Catalog))

    return _g


def _get_dataset_by_url(url: str) -> Graph:
    _g = Graph().parse(url)

    if _g is None or len(_g) == 0:
        raise FetchFromServiceException(
            status=500,
            message=f"Error when attempting to parse dataset with url {url}",
        )
    return _g
