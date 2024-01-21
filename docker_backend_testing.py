import requests


def test_dockerized_app():
    url = "http://127.0.0.1:5000/users/1"  # Adjust URL as needed
    response = requests.get(url)
    assert response.status_code == 200, "Unexpected response status code"
    # assert "users" in response.json(), "Expected 'users' in response JSON"


if __name__ == "__main__":
    test_dockerized_app()
