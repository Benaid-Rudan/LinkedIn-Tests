import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from conftest import browser

@pytest.mark.usefixtures("browser")
class TestLogOut:
    def test_search_user(self, browser):
        # Open the LinkedIn website
        browser.get("https://www.linkedin.com/login")

        # Log in to LinkedIn 
        username_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "username")))
        username_input.send_keys("benaid.rudan@edu.fit.ba")

        password_input = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "password")))
        password_input.send_keys("bakestarmo 12")

        password_input.send_keys(Keys.RETURN)

        WebDriverWait(browser, 20).until(EC.title_contains("LinkedIn"))

        parent_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "global-nav__me")))
        post_popup_button = parent_element.find_element(By.TAG_NAME, "button")
        post_popup_button.click()

        parent_div = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "artdeco-dropdown__content-inner")))
        ul_element = parent_div.find_element(By.CLASS_NAME, "global-nav__secondary-items")
        sign_out_link = ul_element.find_element(By.XPATH, "//a[@class='global-nav__secondary-link mv1' and text()='Sign Out']")
        sign_out_link.click()
        time.sleep(5)
        modal = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "artdeco-modal__content")))

        # Find and click on the "Sign out" button within the modal
        
        modal2 = modal.find_element(By.CLASS_NAME, "p5")
        modal_div = modal2.find_element(By.CLASS_NAME, "mt5")
        signout = modal_div.find_element(By.CLASS_NAME, "artdeco-button")
        signout.click()
        time.sleep(5)
        assert "LinkedIn: Log In or Sign Up" in browser.title
