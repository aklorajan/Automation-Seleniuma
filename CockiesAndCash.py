import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


os.environ['PATH'] += r'c:/'
driver = webdriver.Chrome()

WebDriverWait(driver=driver, timeout=30).until(
    EC.text_to_be_present_in_element(By.XPATH, "//*[@id='hdgfcsygh']"),
    'complete'
)
