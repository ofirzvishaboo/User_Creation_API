import requests


def test_dockerized_app():
    url = "http://192.168.99.100:5000/users/"  # Adjust URL as needed
    response = requests.get(url)
    assert response.status_code == 200, "Unexpected response status code"
    assert "users" in response.json(), "Expected 'users' in response JSON"


if __name__ == "__main__":
    test_dockerized_app()
