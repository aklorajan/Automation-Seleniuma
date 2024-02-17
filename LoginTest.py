from selenium import webdriver
from Login import Login
from time import sleep
import unittest


class LogingTests(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()

    def testValidLogin(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login = Login(driver=self.driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        sleep(5)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
