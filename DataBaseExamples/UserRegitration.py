import sqlite3
from selenium import webdriver

# Connect to SQLite database
conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()

# Create a table to store user information
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY, username TEXT, email TEXT)''')

# Insert dummy user data into the database
cursor.execute("INSERT INTO users (username, email) VALUES ('testuser', 'test@example.com')")
conn.commit()

# Launch the web browser using Selenium WebDriver
driver = webdriver.Chrome()

# Navigate to the profile page
driver.get('https://example.com/profile')

# Extract user information from the web page
username_element = driver.find_element_by_id('username')
email_element = driver.find_element_by_id('email')
web_username = username_element.text
web_email = email_element.text

# Retrieve user information from the database
cursor.execute("SELECT username, email FROM users WHERE id = 1")  # Assuming user ID 1
db_username, db_email = cursor.fetchone()

# Compare data obtained from the web page with data from the database
if web_username == db_username and web_email == db_email:
    print("Validation successful: User data on the web matches the database.")
else:
    print("Validation failed: User data on the web does not match the database.")

# Close the browser and database connection
driver.quit()
conn.close()
