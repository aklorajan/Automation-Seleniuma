# import os.path
#
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.common.by import By
# from time import sleep
# from pathlib import Path
# from selenium.webdriver.firefox.options import Options



# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options)
# # firefoxOption = Options()
# # firefoxOption.add_argument("--headless")
# # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
# # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
# # driver = webdriver.Chrome()
# # driver.get(GeckoDriverManager().install())
# driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
#
# # driver.get("https://www.google.com/")
# # driver.find_element('name', 'q').send_keys('wikipedia')
# # widowTitle = driver.title
# # print(widowTitle)
# # sleep(1)
# # driver.get("https://www.wikipedia.com/")
# # sleep(1)
# # driver.back()
# # sleep(1)
# # driver.forward()d
# # driver.forward()d
# # sleep(1)
# # driver.refresh()
# # driver.switch_to.new_window('teb')
# # driver.switch_to.new_window('window')
# # driver.get('https://www.yahoo.com')
# # # print(driver.window_handles)
# # # windowSize = driver.get_window_size()
# # # print(windowSize)
# # # windowWidth = driver.set_window_size(300, 500)
# # # print(windowWidth)
# # driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
# # currentPath = Path(__file__).parent
# # screenShot = os.path.join(str(currentPath), 'pic.png')
# # driver.save_screenshot(screenShot)
# # sleep(5)
#
#
# # driver.quit()
# # driver.find_elements('name', 'oxd-input--active').send_keys('Admin')
# # driver.find_elements('name', 'password').send_keys('admin123')
# # driver.find_elements('class name', 'orangehrm-login-button').click()
# # sleep(5)
# a = driver.find_element('name', 'username')
# a.send_keys('Admin')
# b = driver.find_element('name', 'password')
# b.send_keys('admin123')
# driver.find_element('class name', 'orangehrm-login-button').click()
# sleep(5)
