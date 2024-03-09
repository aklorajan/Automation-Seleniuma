import unittest
from database_operations import connect_to_mysql, validate_transaction
from selenium_actions import make_purchase_with_selenium


class TestIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Connect to MySQL database
        cls.connection = connect_to_mysql()
        if not cls.connection:
            raise Exception("Failed to connect to MySQL database")

    @classmethod
    def tearDownClass(cls):
        # Close the database connection
        cls.connection.close()

    def test_integration(self):
        # Simulate user making a purchase with Selenium
        customer_id = 1  # Assume customer with ID 1 is making the purchase
        product_id = 1  # Assume product with ID 1 is being purchased
        quantity = 2  # Quantity being purchased
        make_purchase_with_selenium(self.connection, customer_id, product_id, quantity)

        # Validate the transaction in the database
        validate_transaction(self.connection, customer_id, product_id, quantity)


if __name__ == '__main__':
    unittest.main()
