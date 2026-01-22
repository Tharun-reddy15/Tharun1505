import requests
geturl = "http://127.0.0.1:5000/users"
response = requests.get(geturl)

print("get status code", response.status_code)
print(response.json())

posturl = "http://127.0.0.1:5000/users"

body1 = {
    "id":"3",
    "name":"tharun"
}

r1 = requests.post(posturl, json=body1);
print("post status code", r1.status_code)
print(r1.json())