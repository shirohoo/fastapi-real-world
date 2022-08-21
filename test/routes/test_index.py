from fastapi.testclient import TestClient
from application.main import create_app

client = TestClient(create_app())


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_say_hello():
    response = client.get("/hello/User")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello User"}
