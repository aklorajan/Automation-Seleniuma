from Locators import *
from selenium.webdriver.common.by import By

class Login:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, user1):
        self.driver.find_element(By.XPATH, username).send_keys(user1)

    def enter_password(self, pass1):
        self.driver.find_element(By.XPATH, password).send_keys(pass1)

    def click_login(self):
        self.driver.find_element("class name", button_class).click()
