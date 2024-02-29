import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from conftest import browser
import time
@pytest.mark.usefixtures("browser")
class TestAddTextPost:
    def test_test3(self, browser):
        # Open the LinkedIn website
        browser.get("https://www.linkedin.com/login")

        # Log in to LinkedIn 
        username_input = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, "username")))
        username_input.send_keys("benaid.rudan@edu.fit.ba")

        password_input = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, "password")))
        password_input.send_keys("bakestarmo 12")

        password_input.send_keys(Keys.RETURN)

        WebDriverWait(browser, 20).until(EC.title_contains("LinkedIn"))

        # Opening post popup
        parent_element = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "share-box-feed-entry__top-bar")))
        post_popup_button = parent_element.find_element(By.TAG_NAME, "button")
        post_popup_button.click()

        post_input = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "ql-editor")))
        post_input.send_keys("New LinkedIn post.")
        publish_button = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "share-actions__primary-action")))
        post_publich = publish_button.find_element(By.CLASS_NAME, "artdeco-button__text")
        post_publich.click()
        time.sleep(10)

        expected_text = "New LinkedIn post."
        post_content = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div.feed-shared-update-v2__description")))
        assert post_content.text == expected_text, f"Očekivani tekst '{expected_text}', ali dobiveno '{post_content.text}'"     
        print("Uspješno ažuriranje feeda:", post_content.text == "New LinkedIn post.")
