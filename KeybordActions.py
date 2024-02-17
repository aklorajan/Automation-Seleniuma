from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
actions = ActionChains(driver=driver)
driver.get('https://google.com')
searchViki = driver.find_element('name', 'q')

actions.key_down(Keys.SHIFT).send_keys_to_element(searchViki, 'vikipedia').key_up(Keys.SHIFT).send_keys(
    'vikipedia').perform()
sleep(5)
searchViki.click()
actions.key_down(Keys.CONTROL).send_keys('a').send_keys(Keys.DELETE).perform()
sleep(3)
actions.double_click(searchViki)