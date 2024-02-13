import requests

res = requests.put("http://localhost/users/1", json={'user_name': 'ofir'})
print(res.status_code)
