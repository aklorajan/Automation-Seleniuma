import sqlite3
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Connect to SQLite database
conn = sqlite3.connect('booking_database.db')
cursor = conn.cursor()

# Create a table to store booking information
cursor.execute('''CREATE TABLE IF NOT EXISTS bookings
                (booking_id INTEGER PRIMARY KEY, user_id INTEGER, movie_id INTEGER, seat_number TEXT)''')
conn.commit()

# Launch the web browser using Selenium WebDriver
driver = webdriver.Chrome()

# Navigate to the booking page
driver.get('https://example.com/booking')

# Function to select seats using Selenium
def select_seats(seat_numbers):
    for seat_number in seat_numbers:
        seat_element = driver.find_element(By.XPATH, f"//div[@id='seat-map']//div[@data-seat-number='{seat_number}']")
        seat_element.click()

# Function to retrieve the latest booking from the database
def get_latest_booking():
    cursor.execute("SELECT user_id, movie_id, seat_number FROM bookings ORDER BY booking_id DESC LIMIT 1")
    return cursor.fetchone()

# Dummy user-selected seats
selected_seats = ['A1', 'A2', 'B3']

# Select seats and validate against database
select_seats(selected_seats)
time.sleep(2)  # Wait for the seat selection to be processed (simulation)
latest_booking = get_latest_booking()

if latest_booking == (None, None, 'A1') or latest_booking == (None, None, 'A2') or latest_booking == (None, None, 'B3'):
    print("Validation successful: Seats selected are recorded in the database.")
else:
    print("Validation failed: Seats selected are not recorded in the database.")

# Close the browser and database connection
driver.quit()
conn.close()
