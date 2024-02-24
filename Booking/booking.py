import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# service = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:/", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def accept_cookie(self):
        try:
            self.find_element(By.XPATH, const.el_cookie_xpath).click()
        except:
            print('No Cookies')

    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        self.find_element(By.CSS_SELECTOR, const.el_curr_css).click()
        self.find_element(By.XPATH, f"//div[contains(@class,' ea1163d21f') and text()='{currency}']").click()
        sleep(5)

