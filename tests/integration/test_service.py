"""Unit test cases for the fdk_baseregistries_publisher service module."""
from flask import Flask
import pytest


@pytest.mark.integration
def test_fetch_fetch_baseregistries(client: Flask) -> None:
    """Should return a Graph."""
    response = client.get("/baseregistries")
    assert response.status_code == 200
    assert "text/turtle; charset=utf-8" == response.headers["Content-Type"]


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
