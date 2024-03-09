from selenium import webdriver
from Login import Login
from time import sleep
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.service import Service


class LogingTests(webdriver.Chrome, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ChromeDriverManager().setup()
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def testValidLogin(self):
        self.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login = Login(driver=self)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        sleep(5)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.close()
        cls.quit()


if __name__ == "__main__":
    unittest.main()
