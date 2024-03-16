import unittest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Locators import *
from selenium.webdriver.common.by import By


class LoginTestCase(webdriver.Chrome, unittest.TestCase):

    @classmethod
    def setUp(cls, driver_path=r"C:/"):
        # Launch the browser
        cls.driver_path = driver_path
        os.environ['PATH'] += cls.driver_path
        service = Service(ChromeDriverManager().install())
        super(LoginTestCase, cls).__init__(service=service)
        cls.implicitly_wait(10)
        cls.maximize_window()

        # Open the website
        cls.get("https://www.example.com")

    def test_login_valid(self):
        # Find the username and password fields
        username_field = self.find_element(By.XPATH, "username")
        password_field = self.find_element(By.XPATH, "password")
        submit_button = self.find_element(By.ID, "submit")

        # Enter valid username and password
        username_field.send_keys("valid_username")
        password_field.send_keys("valid_password")

        # Click the login button
        submit_button.click()

        # Verify that login was successful
        welcome_message = self.find_element_by_xpath("//div[@id='welcome']")
        self.assertEqual(welcome_message.text, "Welcome, valid_username!")

    def test_login_invalid(self):
        # Find the username and password fields
        username_field = self.find_element_by_id("username")
        password_field = self.find_element_by_id("password")
        submit_button = self.find_element_by_id("submit")

        # Enter invalid username and password
        username_field.send_keys("invalid_username")
        password_field.send_keys("invalid_password")

        # Click the login button
        submit_button.click()

        # Verify that error message is displayed
        error_message = self.find_element_by_xpath("//div[@id='error']")
        self.assertEqual(error_message.text, "Invalid username or password. Please try again.")

    @classmethod
    def tearDown(self):
        # Close the browser
        self.quit()


if __name__ == "__main__":
    unittest.main()
