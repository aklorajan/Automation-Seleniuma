# we have a web application for an online store. We want to simulate the process of a user making a purchase,
# and then validate that the transaction is correctly recorded in a MySQL database using mysql.connector.

import mysql.connector
from mysql.connector import Error
from datetime import datetime


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


def make_purchase(connection, customer_id, product_id, quantity):
    try:
        cursor = connection.cursor()

        # Retrieve product price
        cursor.execute("SELECT price FROM products WHERE product_id = %s", (product_id,))
        price = cursor.fetchone()[0]

        # Calculate total amount
        total_amount = price * quantity

        # Insert order into the database
        cursor.execute("""
            INSERT INTO orders (customer_id, product_id, quantity, total_amount, order_date)
            VALUES (%s, %s, %s, %s, %s)
        """, (customer_id, product_id, quantity, total_amount, datetime.now()))

        connection.commit()
        print('Purchase completed successfully')
    except Error as e:
        print(f'Error making purchase: {e}')


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
                    f'Product ID: {latest_order[0]}, Quantity: {latest_order[1]}, Total Amount: {latest_order[2]}, '
                    f'Order Date: {latest_order[3]}')
            else:
                print('Validation failed: Transaction not recorded correctly in the database')
        else:
            print('Validation failed: No transaction recorded for the customer')
    except Error as e:
        print(f'Error validating transaction: {e}')
