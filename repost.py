import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from conftest import browser
import time
@pytest.mark.usefixtures("browser")
class TestRepost:
    def test_like_post(self, browser):
        # Open the LinkedIn website
        browser.get("https://www.linkedin.com/login")

        # Log in to LinkedIn 
        username_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "username")))
        username_input.send_keys("benaid.rudan@edu.fit.ba")

        password_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "password")))
        password_input.send_keys("bakestarmo 12")

        password_input.send_keys(Keys.RETURN)

        WebDriverWait(browser, 30).until(EC.title_contains("LinkedIn"))

        repost_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "social-reshare-button")))
        repost_button.click()
        time.sleep(5)

        repost_options = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "artdeco-dropdown__content-inner")))
        repost_dropdown = repost_options.find_element(By.CLASS_NAME,"artdeco-dropdown__item")
        repost = repost_dropdown.find_element(By.CLASS_NAME,"t-14")
        repost.click()

        repost_modal = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "share-box")))
        repost_modal_view = repost_modal.find_element(By.CLASS_NAME,"artdeco-modal__content")
        repost_modal_view2 = repost_modal_view.find_element(By.CLASS_NAME,"share-creation-state__bottom")
        footer_modal = repost_modal_view2.find_element(By.CLASS_NAME,"share-creation-state__footer")
        post_container = footer_modal.find_element(By.CLASS_NAME,"share-creation-state__schedule-and-post-container")
        post_button = post_container.find_element(By.CLASS_NAME,"share-box_actions")
        post_button.click()
        time.sleep(5)
        

        # Wait for the toast message to be visible
        toast_message = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "artdeco-toast-item__message"))
        )

        # Get the text content of the span inside the toast message
        actual_text = toast_message.find_element(By.TAG_NAME, "span").text

        # Assert the text matches the expected value
        assert actual_text == "Repost successful.", f"Expected: 'Repost successful', Actual: '{actual_text}'"