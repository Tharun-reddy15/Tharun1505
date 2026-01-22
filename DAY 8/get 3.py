import requests

geturl3 = "import requests"

geturl3 = "https://api.restful-api.dev/objects/7"
response = requests.get(geturl3)

print(response.status_code)
print(response.json())
