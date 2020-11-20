import requests

s = requests.session()

url = s.get("http://45.79.43.178/source_carts/wordpress/wp-admin/", data = {'email': 'admin',
    'password': '123456aA',
})
print(url.text)
