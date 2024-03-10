from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from JiraIntegration import JiraIntegration
from DatabaseIntegration import DatabaseIntegration

# Jira configuration
JIRA_SERVER = 'https://your-jira-instance.atlassian.net'
JIRA_USERNAME = 'your_username'
JIRA_API_TOKEN = 'your_api_token'
JIRA_PROJECT_KEY = 'PROJ'

# Database configuration
DB_HOST = 'localhost'
DB_USERNAME = 'your_db_username'
DB_PASSWORD = 'your_db_password'
DB_DATABASE = 'your_database_name'

# Selenium configuration
BROWSER_DRIVER_PATH = '/path/to/chromedriver'
WEBSITE_URL = 'https://example.com/register'
NEW_USERNAME = 'new_user'
NEW_EMAIL = 'new_user@example.com'
NEW_PASSWORD = 'password123'

# Initialize Jira integration
jira = JiraIntegration(JIRA_SERVER, JIRA_USERNAME, JIRA_API_TOKEN, JIRA_PROJECT_KEY)

# Initialize database integration
db = DatabaseIntegration(DB_HOST, DB_USERNAME, DB_PASSWORD, DB_DATABASE)

# Create a new issue for the registration test case in Jira
issue = jira.create_test_case('Automated Test: User Registration', 'Automated test for user registration process.')


# Selenium test: Register a new user
def register_new_user():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(WEBSITE_URL)
    # Fill in registration form fields and submit
    username_field = driver.find_element_by_id('username')
    email_field = driver.find_element_by_id('email')
    password_field = driver.find_element_by_id('password')
    confirm_password_field = driver.find_element_by_id('confirm_password')
    username_field.send_keys(NEW_USERNAME)
    email_field.send_keys(NEW_EMAIL)
    password_field.send_keys(NEW_PASSWORD)
    confirm_password_field.send_keys(NEW_PASSWORD)
    confirm_password_field.submit()
    time.sleep(2)  # Wait for the page to load
    # Check if registration is successful
    success_message = driver.find_element_by_css_selector('.success-message').text
    driver.quit()
    return 'Registration successful' in success_message


# Run the Selenium test
registration_result = register_new_user()

# Update Jira issue with test result
if registration_result:
    jira.jira.transition_issue(issue, 'Pass')  # Update Jira issue status to "Pass"
    # Store user information in the database
    db.create_user(NEW_USERNAME, NEW_EMAIL, NEW_PASSWORD)
else:
    jira.jira.transition_issue(issue, 'Fail')  # Update Jira issue status to "Fail"
    # Create a bug report in Jira
    bug_issue = jira.jira.create_issue(project=JIRA_PROJECT_KEY, summary='Bug: Registration failed',
                                       description='The user registration process failed during automated testing.')

# Close database connection
db.close_connection()
