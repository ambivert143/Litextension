import MySQLdb
import csv

mydb = MySQLdb.connect(host='127.0.0.1', user='root', password='', database='docfile')
with open('customer.csv') as csv_file:
    csvfile = csv.reader(csv_file, delimiter=',')
    all_value = []
    for row in csvfile:
        value = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12])
        all_value.append(value)

query = "insert into 'tbl_customer' {`customerid`, `firstname` ,`lastname` ,`companyname` ,`billingaddress1` ,`billingaddress2`,`city`,`state`,`postalcode`,`country`,`phonenumber`,`emailaddress`,`createddate`} value (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "

mycursor = mydb.cursor()
mycursor.executemany(query, all_value)
mydb.commit()