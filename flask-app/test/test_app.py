from flask_app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, Jenkins CI/CD!" in response.data
