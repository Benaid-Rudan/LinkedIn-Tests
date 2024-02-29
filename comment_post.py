import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from conftest import browser

@pytest.mark.usefixtures("browser")
class TestCommentPost:
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

        parent_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "comment-button")))
        parent_element.click()

        comment_input = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "ql-editor")))
        comment_input.send_keys("Automated Python!")
        publish_button = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "comments-comment-box__submit-button")))
        publish_button.click()

        # Provjera uspješnog ažuriranja feeda
        post_content = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "article.comments-comment-item")))
        print("Successfully published comment:", post_content.text == "Automated Python!")

        parent_div=post_content.find_element(By.CLASS_NAME,"update-components-text")
        child_div=parent_div.find_element(By.TAG_NAME,"span")
        child_text=child_div.text
        # Assertion to check if the comment was successfully published
        assert child_text == "Automated Python!", "Comment was not successfully published!"
