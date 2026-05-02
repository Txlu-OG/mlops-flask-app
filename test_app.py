from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_prediction():
    client = app.test_client()
    response = client.post(
        "/predict",
        json={"features": [2, 3, 4, 5]},
    )
    assert response.status_code == 200
    