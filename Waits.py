from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


# def waitElementHasAttribute(elSelector, elLocator, attribute, attributeValue, timeout=7, exact=True):
#     for i in range(timeout * 5):
#         try:
#             element = driver.find_element(elSelector, elLocator)
#             if exact:
#                 assert element.get_attribute(attribute) == attributeValue
#             else:
#                 assert attributeValue in element.get_attribute(attribute)
#             print(f'Element attribute met {str(attribute)}')
#             return
#         except:
#             sleep(0.2)
#     raise Exception(f'element attribute is not {str(attribute)}')


driver.get('https://play1.automationcamp.ir/expected_conditions.html')
triggerEl = driver.find_element(By.ID, 'enabled_trigger')
triggerEl.location_once_scrolled_into_view
triggerEl.click()
wait = WebDriverWait(driver=driver, timeout=5)
el = wait.until(EC.element_to_be_clickable((By.ID, 'enabled_target')))
print(el)

# waitElementHasAttribute(By.ID, 'enabled_target', 'class ', 'success', exact=True)


# def waitElementHasNotAttribute(elSelector, elLocator, attribute, attributeValue, timeout=7, exact=True):
#     for i in range(timeout * 5):
#         try:
#             element = driver.find_element(elSelector, elLocator)
#             if exact:
#                 assert element.get_attribute(attribute) != attributeValue
#             else:
#                 assert attributeValue not in element.get_attribute(attribute)
#             print(f'Element attribute met {str(attribute)}')
#             return
#         except:
#             sleep(0.2)
#     raise Exception(f'element attribute is not {str(attribute)}')



