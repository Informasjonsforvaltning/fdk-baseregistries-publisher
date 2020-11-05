"""Integration test cases for the ready route."""
from flask import Flask
import pytest


@pytest.mark.integration
def test_ready(client: Flask) -> None:
    """Should return 200 and OK."""
    response = client.get("/ready")

    assert response.status_code == 200
    assert response.data.decode() == "OK"
