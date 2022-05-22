import json
import requests

BASE = "http://127.0.0.1:5000"
data = {"email":"jt", "password":"1234"}
data = {"token": "000000"}
response = requests.get(url=(BASE + "/querytwo"), 
                        data=json.dumps(data),
                        headers={"Content-Type":"application/json"})

print(response)
print(response.json())