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
TARGET_PROFILE_URL = "https://www.linkedin.com/company/the-coca-cola-company/"

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # You can use other drivers like Edge
    yield driver
    driver.quit()

def test_login_and_follow_company(browser):
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
    time.sleep(5)   # You might want to replace this sleep with WebDriverWait for a specific element

    # Navigate to the target company profile
    browser.get(TARGET_PROFILE_URL)

    # Find the Follow button and click on it
    follow_button = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "follow"))
    )
    follow_button.click()
    time.sleep(5)
    assert follow_button.text == "Following", "Validation failed: The 'Follow' button did not change to 'Following'"