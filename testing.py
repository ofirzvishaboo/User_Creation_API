import requests

res = requests.get("http://0.0.0.0:3000/users/1")
print(res.json())
