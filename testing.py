import requests

res = requests.post("http://devops-rest:3000/users/5", json={'user_name': 'ofir'})
print(res.status_code)
