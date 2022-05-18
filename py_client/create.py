import json
import requests
endpoint = "http://localhost:8000/api/products/"

get_response = requests.post(endpoint, json={
    "title":"Title 5",
    "price":345.0
})

print(get_response.json())
print(get_response.status_code)
