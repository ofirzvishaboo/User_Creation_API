import requests

res = requests.post("http://localhost:3000/users/5", json={'user_name': 'ofir'})
print(res.status_code)
