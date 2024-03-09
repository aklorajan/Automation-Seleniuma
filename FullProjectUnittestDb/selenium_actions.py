from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from database_operations import make_purchase


def make_purchase_with_selenium(connection, customer_id, product_id, quantity):
    try:
        driver = webdriver.Chrome()
        driver.get('https://example.com')  # Replace with the URL of the online store

        # Simulate user browsing and adding product to cart
        product_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[@data-product-id='{product_id}']"))
        )
        product_element.click()

        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Cart']"))
        )
        add_to_cart_button.click()

        # Proceed to checkout
        checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Checkout']"))
        )
        checkout_button.click()

        # Complete checkout and record transaction in the database
        make_purchase(connection, customer_id, product_id, quantity)

        print('Purchase completed successfully with Selenium')
    except Exception as e:
        print(f'Error making purchase with Selenium: {e}')
    finally:
        driver.quit()
