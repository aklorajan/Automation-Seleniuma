import sqlite3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Connect to SQLite database
conn = sqlite3.connect('feedback_database.db')
cursor = conn.cursor()

# Create a table to store feedback information
cursor.execute('''CREATE TABLE IF NOT EXISTS feedback
                (id INTEGER PRIMARY KEY, name TEXT, email TEXT, message TEXT)''')
conn.commit()

# Launch the web browser using Selenium WebDriver
driver = webdriver.Chrome()

# Navigate to the feedback form page
driver.get('https://example.com/feedback')

# Fill out the feedback form using Selenium WebDriver
name_input = driver.find_element_by_id('name')
email_input = driver.find_element_by_id('email')
message_input = driver.find_element_by_id('message')

name_input.send_keys('John Doe')
email_input.send_keys('johndoe@example.com')
message_input.send_keys('This is a test feedback message.')

# Submit the feedback form
message_input.send_keys(Keys.RETURN)

# Retrieve the submitted feedback from the database
cursor.execute("SELECT name, email, message FROM feedback WHERE id = (SELECT MAX(id) FROM feedback)")
db_name, db_email, db_message = cursor.fetchone()

# Compare data obtained from the web form with data from the database
if db_name == 'John Doe' and db_email == 'johndoe@example.com' and db_message == 'This is a test feedback message.':
    print("Validation successful: Feedback submitted on the web matches the database.")
else:
    print("Validation failed: Feedback submitted on the web does not match the database.")

# Close the browser and database connection
driver.quit()
conn.close()
