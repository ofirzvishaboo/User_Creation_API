import requests

res = requests.delete("http://localhost/users/1")
print(res.status_code)
