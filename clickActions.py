from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
actions = ActionChains(driver=driver)

driver.get('https://trytestingthis.netlify.app/')
el1 = driver.find_element(By.XPATH, '//*[text()="Double-click me"]')
actions.double_click(el1).perform()
sleep(5)

