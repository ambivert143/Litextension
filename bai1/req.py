import requests

data = dict(username='admin',password='123456aA')

s= requests.session()
s.get("http://45.79.43.178/source_carts/wordpress/wp-admin/profile.php")

res = s.get('http://45.79.43.178/source_carts/wordpress/wp-login.php?redirect_to=http%3A%2F%2F45.79.43.178%2Fsource_carts%2Fwordpress%2Fwp-admin%2F&reauth=1', data=data)

print(res.text)
"""
import requests
from bs4 import BeautifulSoup

url = "http://45.79.43.178/source_carts/wordpress/wp-admin"
login = "http://45.79.43.178/source_carts/wordpress/wp-login.php"
username = 'admin'
password = '123456aA'
key = {'log':username, 'pwd':password, 'wp-submit':'Log in', 'redirect_to':url,'testcookie':'1'}
res = requests.post(login, data=key)
soup = BeautifulSoup(res.text)
mydivs = soup.findAll('span',{'class':'display-name'})
print(mydivs)"""