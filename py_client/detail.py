import json
import requests
endpoint = "http://localhost:8000/api/products/detail/1"

get_response = requests.get(endpoint)
print(get_response.json())
print(get_response.status_code)
