import requests

geturl2 = "import requests"

geturl2 = "https://api.restful-api.dev/objects?id=3&id=5&id=10"
response = requests.get(geturl2)

print(response.status_code)
print(response.json())
