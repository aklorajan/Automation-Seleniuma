import os.path

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from pathlib import Path
from selenium.webdriver.firefox.options import Options

firefoxOption = Options()
firefoxOption.add_argument("--headless")
# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefoxOption)
# driver.get("https://www.google.com/")
# driver.find_element('name', 'q').send_keys('wikipedia')
# widowTitle = driver.title
# print(widowTitle)
# sleep(1)
# driver.get("https://www.wikipedia.com/")
# sleep(1)
# driver.back()
# sleep(1)
# driver.forward()d
# driver.forward()d
# sleep(1)
# driver.refresh()
# driver.switch_to.new_window('teb')
# driver.switch_to.new_window('window')
driver.get('https://www.yahoo.com')
# print(driver.window_handles)
# windowSize = driver.get_window_size()
# print(windowSize)
# windowWidth = driver.set_window_size(300, 500)
# print(windowWidth)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
currentPath = Path(__file__).parent
screenShot = os.path.join(str(currentPath), 'pic.png')
driver.save_screenshot(screenShot)
sleep(5)


driver.quit()
