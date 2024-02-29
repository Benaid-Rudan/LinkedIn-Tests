import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

@pytest.mark.usefixtures("browser")
class TestUserSearch:
    def test_search_user(self, browser):
        # Open the LinkedIn website
        browser.get("https://www.linkedin.com/login")

        # Log in to LinkedIn 
        username_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "username")))
        username_input.send_keys("benaid.rudan@edu.fit.ba")

        password_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "password")))
        password_input.send_keys("bakestarmo 12")

        password_input.send_keys(Keys.RETURN)

        WebDriverWait(browser, 10).until(EC.title_contains("LinkedIn"))

        # Search for Adil Eminagić
        search_input = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "search-global-typeahead__input")))
        search_input.send_keys("Adil Eminagić")
        search_input.send_keys(Keys.RETURN)
        
        time.sleep(15)   

        assert "Adil Eminagić" in browser.title  