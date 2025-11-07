import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_route(client):
    """Test the root endpoint returns HTML and status 200."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello Felix" in response.data
    assert b"Flask webserver" in response.data


def test_health_route(client):
    """Test the /health endpoint returns correct JSON."""
    response = client.get('/health')
    json_data = response.get_json()

    assert response.status_code == 200
    assert isinstance(json_data, dict)
    assert json_data["status"] == "healthy"
    assert json_data["service"] == "flask-app"
    assert json_data["uptime"] == "OK"
