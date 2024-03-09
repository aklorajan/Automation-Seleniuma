import mysql.connector
import unittest
from mysql.connector import Error
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Function to connect to the MySQL database
def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='online_store',
            user='username',
            password='password'
        )
        if connection.is_connected():
            print('Connected to MySQL database')
            return connection
    except Error as e:
        print(f'Error connecting to MySQL database: {e}')
        return None


# Function to simulate a user making a purchase with Selenium
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


# Function to validate the transaction in the database
def validate_transaction(connection, customer_id, product_id, quantity):
    try:
        cursor = connection.cursor()

        # Retrieve latest order for the customer
        cursor.execute("""
            SELECT product_id, quantity, total_amount, order_date
            FROM orders
            WHERE customer_id = %s
            ORDER BY order_id DESC
            LIMIT 1
        """, (customer_id,))
        latest_order = cursor.fetchone()

        if latest_order:
            if latest_order[0] == product_id and latest_order[1] == quantity:
                print('Validation successful: Transaction recorded in the database')
                print(
                    f'Product ID: {latest_order[0]}, Quantity: {latest_order[1]}, Total Amount: {latest_order[2]}, Order Date: {latest_order[3]}')
            else:
                print('Validation failed: Transaction not recorded correctly in the database')
        else:
            print('Validation failed: No transaction recorded for the customer')
    except Error as e:
        print(f'Error validating transaction: {e}')


# Define a unittest class for testing
class TestPurchase(unittest.TestCase):

    def setUp(self):
        self.connection = connect_to_mysql()
        if not self.connection:
            self.fail('Failed to connect to MySQL database')

    def tearDown(self):
        if self.connection:
            self.connection.close()

    def test_purchase(self):
        # Simulate user making a purchase with Selenium
        customer_id = 1  # Assume customer with ID 1 is making the purchase
        product_id = 1  # Assume product with ID 1 is being purchased
        quantity = 2  # Quantity being purchased
        make_purchase_with_selenium(self.connection, customer_id, product_id, quantity)

        # Validate the transaction in the database
        validate_transaction(self.connection, customer_id, product_id, quantity)


if __name__ == "__main__":
    unittest.main()
