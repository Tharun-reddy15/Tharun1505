import requests

geturl = "https://api.restful-api.dev/objects"
response = requests.get(geturl)

print(response.status_code)
print(response.json())