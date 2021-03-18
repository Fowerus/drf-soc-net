import requests
import json

headers = json.loads({"Content-Type":"application/json"}) 

r = requests.post('http://127.0.0.1:8000/users/auth/login/', data = {'email':'user1','password':'user1user1'}, headers = headers)
print(r.text)