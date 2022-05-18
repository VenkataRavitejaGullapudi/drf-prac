import json
import requests
endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, params={
    "abc": 123
}, json={
    "title":"Title 1",
    "content": "Hello"
})

print(get_response.json())
print(get_response.status_code)
