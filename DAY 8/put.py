import requests
puturl = "https://api.restful-api.dev/objects/ff8081819782e69e019be443a64b3008"


body1 = {
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
   }
}

r1 = requests.put(puturl, json=body1);
print("put status code", r1.status_code)
print(r1.json())

