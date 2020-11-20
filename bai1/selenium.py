from selenium import webdriver
from webdriver_manager.edge import EdgeDriverManager

driver = webdriver.Edge('./edgedriver')
driver.get('http://45.79.43.178/source_carts/wordpress/wp-admin/')
print(driver)