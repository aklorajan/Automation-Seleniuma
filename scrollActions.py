from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


# def scrollToFindElement(locator, pixel):
#     for i in range(10):
#         try:
#             driver.find_element(locator[0], locator[1])
#             return f'the element {locator[1]} is in list'
#         except:
#             driver.execute_script(f'window.scrollBy(0,{str(pixel)})')
#     raise Exception(f'Element {locator[1]} does not exists')
#
#
driver.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
# # sleep(10)
# # driver.find_element(By.XPATH, "//*[contains(@class,'dRCGjd')]").click()
# result = scrollToFindElement(['xpath', '//*[text() = "196. Dead Poets Society"]'], 2000)
# print(result)
# sleep(3)
el = driver.find_element('xpath', '//*[text() = "196. Dead Poets Society"]')
driver.execute_script('arguments[0].scrollIntoView()', el)
sleep(5)


#  vertical Scroll
driver.execute_script("document.getElementById('quantity').scrollIntoView()")
#  horizontal scroll
driver.execute_script("document.querySelector('table td:last-child').scrollIntoView()")

actions = ActionChains(driver=driver)
el = driver.find_element('xpath', '//*[text() = "196. Dead Poets Society"]')
el.location_once_scrolled_into_view