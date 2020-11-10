"""Contract test cases for baseregistries."""
from typing import Any

import pytest
from rdflib import Graph
from rdflib.compare import graph_diff
import requests


@pytest.mark.contract
def test_baseregistries(http_service: Any) -> None:
    """Should return OK."""
    url = f"{http_service}/baseregistries"
    response = requests.get(url)

    assert response.status_code == 200
    assert 200 == response.status_code
    assert 0 < len(response.content)
    assert "text/turtle; charset=utf-8" == response.headers["Content-Type"]
    g1 = Graph()
    g1.parse(data=response.text, format="turtle")
    assert 0 < len(g1)


# ---------------------------------------------------------------------- #
# Utils for displaying debug information


def _dump_diff(g1: Graph, g2: Graph) -> None:
    in_both, in_first, in_second = graph_diff(g1, g2)
    print("\nin both:")
    _dump_turtle(in_both)
    print("\nin first:")
    _dump_turtle(in_first)
    print("\nin second:")
    _dump_turtle(in_second)


def _dump_turtle(g: Graph) -> None:
    for _l in g.serialize(format="turtle").splitlines():
        if _l:
            print(_l.decode())
