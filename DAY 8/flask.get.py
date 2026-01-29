import requests

geturl="http://127.0.0.1:5002/users"
response=requests.get(geturl)

print("get status code",response.status_code)
print(response.json())