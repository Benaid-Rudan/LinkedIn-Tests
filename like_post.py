import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from conftest import browser

@pytest.mark.usefixtures("browser")
class TestLikePost:
    def test_like_post(self, browser):
        # Open the LinkedIn website
        browser.get("https://www.linkedin.com/login")

        # Log in to LinkedIn 
        username_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "username")))
        username_input.send_keys("benaid.rudan@edu.fit.ba")

        password_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "password")))
        password_input.send_keys("bakestarmo 12")

        password_input.send_keys(Keys.RETURN)

        WebDriverWait(browser, 10).until(EC.title_contains("LinkedIn"))

        # Opening post popup
        parent_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "reactions-react-button")))
        like_button = parent_element.find_element(By.TAG_NAME, "button")
        like_button.click()