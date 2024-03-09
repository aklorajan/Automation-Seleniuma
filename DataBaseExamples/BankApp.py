import sqlite3
import time
from selenium import webdriver

# Connect to SQLite database
conn = sqlite3.connect('transactions_database.db')
cursor = conn.cursor()

# Create a table to store transaction information
cursor.execute('''CREATE TABLE IF NOT EXISTS transactions
                (id INTEGER PRIMARY KEY, sender_account TEXT, receiver_account TEXT, amount REAL)''')
conn.commit()

# Launch the web browser using Selenium WebDriver
driver = webdriver.Chrome()

# Navigate to the banking application
driver.get('https://example.com/banking')

# Function to initiate a money transfer using Selenium
def initiate_transfer(sender_account, receiver_account, amount):
    sender_input = driver.find_element_by_id('sender_account')
    receiver_input = driver.find_element_by_id('receiver_account')
    amount_input = driver.find_element_by_id('amount')
    submit_button = driver.find_element_by_id('submit_button')

    sender_input.send_keys(sender_account)
    receiver_input.send_keys(receiver_account)
    amount_input.send_keys(amount)
    submit_button.click()

# Function to retrieve the latest transaction from the database
def get_latest_transaction():
    cursor.execute("SELECT sender_account, receiver_account, amount FROM transactions ORDER BY id DESC LIMIT 1")
    return cursor.fetchone()

# Dummy user-initiated transfers
transfers = [
    {'sender_account': '123456', 'receiver_account': '789012', 'amount': 100.00},
    {'sender_account': '789012', 'receiver_account': '123456', 'amount': 50.00}
]

# Perform transfers and validate against database
for transfer in transfers:
    initiate_transfer(transfer['sender_account'], transfer['receiver_account'], transfer['amount'])
    time.sleep(2)  # Wait for the transaction to be processed (simulation)
    latest_transaction = get_latest_transaction()

    if latest_transaction == (transfer['sender_account'], transfer['receiver_account'], transfer['amount']):
        print("Validation successful: Transaction recorded in the database matches the initiated transfer.")
    else:
        print("Validation failed: Transaction recorded in the database does not match the initiated transfer.")

# Close the browser and database connection
driver.quit()
conn.close()
