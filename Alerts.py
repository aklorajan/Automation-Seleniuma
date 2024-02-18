from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
alert = Alert(driver=driver)
driver.implicitly_wait(2)


# def pageSource():
#     return driver.page_source


#
# driver.get('https://the-internet.herokuapp.com/javascript_alerts')
# # print(pageSource().title)
#
# driver.find_element(By.XPATH, "//*[text()='Click for JS Prompt']").click()
# alert.send_keys('hellooooo')
# sleep(3)
# alert.accept()
# assert 'hellooooo' in pageSource()
# sleep(3)

# driver.get('https://material.angular.io/components/dialog/examples')

# elOff = driver.find_element(By.XPATH, "//button[@aria-label='Select a version']")
# offset = elOff.location
# driver.find_element(By.XPATH, "//*[text()='Open dialog']/..").click()
# driver.find_element(By.XPATH, "//*[text()='Install']")
# actions = ActionChains(driver=driver)
# actions.move_by_offset(offset['x'], offset['y']).click().pause(2).click().perform()
#
# sleep(5)

driver.get('https://material.angular.io/components/snack-bar/overview')
el = driver.find_element(By.XPATH, "//*[text()='Show snack-bar']")
el.click()
sleep(5)
dom = driver.page_source
# print(dom)
driver.find_element(By.XPATH, "//*[@class='mat-mdc-snack-bar-label mdc-snackbar__label']")
print('Test Passed')
