import requests

puturl="http://127.0.0.1:5000/users/102"
response=requests.put(puturl)

print("put status code",response.status_code)
print(response.json())