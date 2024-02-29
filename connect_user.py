import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from conftest import browser


@pytest.mark.usefixtures("browser")
class TestSendConnectionRequest:
    def test_connect(self, browser):
        # Open the LinkedIn website
        browser.get("https://www.linkedin.com/login")

        # Log in to LinkedIn 
        username_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "username")))
        username_input.send_keys("benaid.rudan@edu.fit.ba")

        password_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "password")))
        password_input.send_keys("bakestarmo 12")

        password_input.send_keys(Keys.RETURN)

        WebDriverWait(browser, 10).until(EC.title_contains("LinkedIn"))

        # Search for user

        search_input = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "search-global-typeahead__input")))
        search_input.send_keys("Selma Korić")
        search_input.send_keys(Keys.RETURN)

        WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "entity-result__universal-image")))

        # Find user profile
        profile_link = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "presence-entity__image")))
        profile_link.click()

        # Send a connection request
        parent_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "rjgCOEVwWPnrtVirBlyyskSIBJIvTyA")))
        connect_button = parent_element.find_element(By.TAG_NAME, "button")
        
        connect_button.click()
        time.sleep(2)
        print(connect_button.text)
        # Wait for the modal with "Send without a note" button
        modal_actions = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "artdeco-modal__actionbar"))
        )

        # Find "Send without a note" button and click it
        send_without_note_button = modal_actions.find_element(By.XPATH, ".//button[contains(@aria-label, 'Send now')]")
        send_without_note_button.click()
        
        time.sleep(2)

        parent_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "rjgCOEVwWPnrtVirBlyyskSIBJIvTyA")))
        post_popup_button = parent_element.find_element(By.TAG_NAME, "button")
        pending_b = post_popup_button.find_element(By.CLASS_NAME, "artdeco-button__text")
        text = pending_b.text

        assert text == "Pending", "Validation failed: The 'Connect' button did not change to 'Pending'"
