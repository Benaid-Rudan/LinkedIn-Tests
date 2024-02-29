import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace these with your actual LinkedIn credentials
USERNAME = "benaid.rudan@edu.fit.ba"
PASSWORD = "bakestarmo 12"

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # You can use other drivers like Edge
    yield driver
    driver.quit()

def test_login_to_linkedin(browser):
    # Open LinkedIn login page
    browser.get("https://www.linkedin.com/login")

    # Find the username and password input fields and submit button
    username_input = browser.find_element("id", "username")
    password_input = browser.find_element("id", "password")
    submit_button = browser.find_element("tag name", "button")
    
    # Enter credentials
    username_input.send_keys(USERNAME)
    password_input.send_keys(PASSWORD)

    # Click the submit button to log in
    submit_button.click()
    time.sleep(15)   
    # Check if the login was successful by verifying the presence of a known element on the home page
    assert "LinkedIn" in browser.title  

# Run the test
# pytest login_linkedin.py
