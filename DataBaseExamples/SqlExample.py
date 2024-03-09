import sqlite3
from selenium import webdriver

# Connect to SQLite database
conn = sqlite3.connect('product_database.db')
cursor = conn.cursor()

# Create a table to store product information
cursor.execute('''CREATE TABLE IF NOT EXISTS products
                (product_id INTEGER PRIMARY KEY, name TEXT, price REAL)''')

# Insert dummy product data into the database
cursor.execute("INSERT INTO products (name, price) VALUES ('Product A', 10.99)")
cursor.execute("INSERT INTO products (name, price) VALUES ('Product B', 20.49)")
conn.commit()

# Launch the web browser using Selenium WebDriver
driver = webdriver.Chrome()

# Navigate to the product page
driver.get('https://example.com/products')

# Extract product information from the web page
product_elements = driver.find_elements_by_class_name('product')
web_product_prices = {}

for product_element in product_elements:
    product_name = product_element.find_element_by_class_name('name').text
    product_price = float(product_element.find_element_by_class_name('price').text.replace('$', ''))
    web_product_prices[product_name] = product_price

# Retrieve product information from the database
cursor.execute("SELECT name, price FROM products")
db_product_prices = {name: price for name, price in cursor.fetchall()}

# Compare data obtained from the web page with data from the database
validation_passed = True

for product_name, web_price in web_product_prices.items():
    db_price = db_product_prices.get(product_name)
    if db_price is None or db_price != web_price:
        print(f"Validation failed for product {product_name}: Database price {db_price} does not match web price {web_price}")
        validation_passed = False

if validation_passed:
    print("Validation successful: Product prices on the web match the database.")

# Close the browser and database connection
driver.quit()
conn.close()
