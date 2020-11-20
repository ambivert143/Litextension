import requests
import csv

r = requests.get('https://675e3c8b15186b223ad0ad7f135a20b8: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@mai-l-ng.myshopify.com/admin/api/2020-10/customers.json')


with open('./bai3/customers_export_1.csv', encoding='utf-8') as f:
    r = f.read()

print(r)