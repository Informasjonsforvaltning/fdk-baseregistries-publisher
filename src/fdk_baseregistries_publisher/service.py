"""Service layer module for fdk_baseregistries_publisher."""
from os import environ as env

from rdflib import DCTERMS, FOAF, Graph, Literal, Namespace, RDF, SKOS, URIRef

from .exceptions.exeption import FetchFromServiceException


BASEREGISTRY_CATALOG_URL = env.get(
    "BASEREGISTRY_CATALOG_URL",
    "https://baseregistries-publisher.fellesdatakatalog.digdir.no",
)

DCAT = Namespace("http://www.w3.org/ns/dcat#")
PROV = Namespace("http://www.w3.org/ns/prov#")
VCARD = Namespace("http://www.w3.org/2006/vcard/ns#")
DQV = Namespace("http://www.w3.org/ns/dqvNS#")
DCATNO = Namespace("http://difi.no/dcatno#")
EUROVOC = Namespace("http://publications.europa.eu/ontology/authority/")

BASEREGISTRY_DATASET_URLS = [
    "https://data.norge.no/datasets/68d08f28-a16d-4fab-a953-ed4ab08ce2e2",
    "https://data.norge.no/datasets/e281c8c6-b944-4662-861d-a475e973e393",
    "https://data.norge.no/datasets/1b4d8a57-008a-4988-803a-fde4a024eae5",
]

catalog = Graph()
baseregister_catalog = URIRef(BASEREGISTRY_CATALOG_URL)


def fetch_baseregistries() -> Graph:
    """Fetch a catalog of datasets representing base registries."""
    _catalog = _create_catalog_graph()
    _registries = Graph()

    for url in BASEREGISTRY_DATASET_URLS:
        _baseregistry = _get_dataset_by_url(url)
        # Get the node for the dataset:
        _baseregistry_url = _baseregistry.value(
            predicate=RDF.type, object=DCAT.Dataset, any=False
        )
        # Add the node to the catalog:
        _catalog.add((baseregister_catalog, DCAT.dataset, _baseregistry_url))
        _registries += _baseregistry
    catalog = _catalog + _registries
    return catalog


def _create_catalog_graph() -> Graph:
    _g = Graph()

    _g.bind("dcat", DCAT)
    _g.bind("dct", DCTERMS)
    _g.bind("skos", SKOS)
    _g.bind("prov", PROV)
    _g.bind("vcard", VCARD)
    _g.bind("foaf", FOAF)
    _g.bind("dqv", DQV)
    _g.bind("dcatno", DCATNO)
    _g.bind("eurovoc", EUROVOC)

    _g.add((baseregister_catalog, RDF.type, DCAT.Catalog))
    # dct:title
    title = Literal("Norwegian base registries", lang="en")
    _g.add((baseregister_catalog, DCTERMS.title, title))
    # dct:description
    description = Literal("Norwegian catalog of national base registries", lang="en")
    _g.add((baseregister_catalog, DCTERMS.description, description))
    # dct:publisher
    publisher = URIRef(
        "https://organization-catalogue.fellesdatakatalog.digdir.no/organizations/991825827"
    )
    _g.add((baseregister_catalog, DCTERMS.publisher, publisher))
    # dct:LinguisticSystem
    ls = URIRef("http://id.loc.gov/vocabulary/iso639-1/nb")
    _g.add((baseregister_catalog, DCTERMS.LinguisticSystem, ls))
    # dct:spatial
    location = URIRef("http://publications.europa.eu/resource/authority/country/NOR")
    _g.add((baseregister_catalog, DCTERMS.spatial, location))

    return _g


def _get_dataset_by_url(url: str) -> Graph:
    _g = Graph().parse(url)

    if _g is None or len(_g) == 0:
        raise FetchFromServiceException(
            status=500,
            message=f"Error when attempting to parse dataset with url {url}",
        )
    return _g
