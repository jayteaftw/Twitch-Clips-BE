from wsgiref import headers
import requests

BASE = "http://127.0.0.1:5000"
response = requests.post(url=(BASE + "/signIn"), data={"email":"jt", "password":"1234"})

print(response)
print(response.json())