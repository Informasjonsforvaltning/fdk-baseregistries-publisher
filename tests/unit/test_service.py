"""Unit test cases for the fdk_baseregistries_publisher service module."""
import pytest
from pytest_mock import MockFixture
from rdflib import Graph


from fdk_baseregistries_publisher.service import (
    fetch_baseregistries,
    FetchFromServiceException,
)


@pytest.mark.unit
def test_fetch_fetch_baseregistries(mocker: MockFixture) -> None:
    """Should return a Graph."""
    g1 = fetch_baseregistries()
    assert isinstance(g1, Graph)


@pytest.mark.unit
def test_fetch_baseregistries_when_parsing_fails(mocker: MockFixture) -> None:
    """Should raise a FetchFromServiceException."""
    mocker.patch("rdflib.Graph.parse", return_value=None)
    with pytest.raises(FetchFromServiceException):
        _ = fetch_baseregistries()


def _mock_queryresult() -> str:
    """Create a mock catalog collection response."""
    response = """
    @prefix dcat: <http://www.w3.org/ns/dcat#> .
    @prefix dct: <http://purl.org/dc/terms/> .
    @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix vcard: <http://www.w3.org/2006/vcard/ns#> .
    @prefix xml: <http://www.w3.org/XML/1998/namespace> .
    @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

    <http://dataservice-publisher:8080/catalogs/1> a dcat:Catalog .
    """
    return response
