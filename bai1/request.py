"""import requests

s = requests.session()

url = s.get("http://45.79.43.178/source_carts/wordpress/wp-admin/", data = {'username': 'admin',
    'password': '123456aA',
})
data1 = repr(url)
username = data1["username"]
password = data1["password"]
print(url.text)
print(password)
print(username)
"""
import requests
#import json

url = "http://45.79.43.178/source_carts/wordpress/wp-admin/"
data = {'email': 'admin',
    'password': '123456aA',
}
s = requests.session()
request = s.get(url, params=data)

print(request.url)
output = request.text
print(output)
#output_dict = json.loads(output)
#print(output_dict.keys())