"""from selenium import webdriver
from webdriver_manager.edge import EdgeDriverManager

driver = webdriver.Edge('./edgedriver')
driver.get('http://45.79.43.178/source_carts/wordpress/wp-admin/')
print(driver)"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import unittest

class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome() #cung cấp đường dẫn thực thi =((
        self.driver.get("http://45.79.43.178/source_carts/wordpress/wp-login.php?redirect_to=http%3A%2F%2F45.79.43.178%2Fsource_carts%2Fwordpress%2Fwp-admin%2F&reauth=1")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        username = "admin"
        password = "123456aA"

        emailFieldID = "email"
        passFeildID = "pass"
        loginButtonXpath = "//input[@value = 'Log In']"

        emailFieldElement = WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_id(emailFieldID))
        passFeildElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFeildID))
        loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(loginButtonXpath))

        emailFieldElement.clear()
        emailFieldElement.send_keys(username)
        passFeildElement.clear()
        passFeildElement.send_keys(password)
        loginButtonElement.click()\

    def tearDown(self):
        self.driver.quit()

if __name__== '__main__':
    unittest.main()