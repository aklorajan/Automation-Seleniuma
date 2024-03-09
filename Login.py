from Locators import *
from selenium.webdriver.common.by import By
from selenium import webdriver


class Login():
    def __init__(self, driver):
        # super(Login, self).__init__()
        self.driver = driver
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def open_webpage(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    def enter_username(self, user1):
        self.driver.find_element(By.XPATH, username).send_keys(user1)

    def enter_password(self, pass1):
        self.driver.find_element(By.XPATH, password).send_keys(pass1)

    def click_login(self):
        self.driver.find_element("class name", button_class).click()
