from fastapi.testclient import TestClient
from app.main import app

def test_people_endpoint(httpx_mock):
    httpx_mock.add_response(
        method="GET",
        url="https://swapi.dev/api/people/",
        json={
            "results": [{"name": "Luke Skywalker"}, {"name": "Darth Vader"}],
            "next": None
        }
    )

    client = TestClient(app)
    response = client.get("/people")

    assert response.status_code == 200
    assert response.json() == {"names": ["Luke Skywalker", "Darth Vader"]}
