import pytest
from pages.login.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
load_dotenv()
@pytest.mark.usefixtures("setup")
class TestLogin:
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.navigate_to()
        login_page.enter_username(self.USERNAME)
        login_page.enter_password(self.PASSWORD)
        # Assert that username and password are correctly entered
        entered_username = login_page.get_username_value()
        entered_password = login_page.get_password_value()

        assert entered_username == self.USERNAME, f"Expected username: {self.USERNAME}, but got: {entered_username}"
        assert entered_password == self.PASSWORD, f"Expected password: {self.PASSWORD}, but got: {entered_password}"

        login_page.click_login_button()
        # Assert successful login by checking the current URL
        WebDriverWait(self.driver, 10).until(
        EC.url_contains("#/dashboard")
        )

         # Assert successful login by checking the current URL
        assert "#/dashboard" in self.driver.current_url, f"Expected '#/dashboard' in URL, but got: {self.driver.current_url}"