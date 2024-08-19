from pages.base_page import BasePage
class LoginPage(BasePage):
    USERNAME_LOCATOR = ("id", "username1")
    PASSWORD_LOCATOR = ("id", "password1")
    LOGINBTN_LOCATOR = ("xpath", "//input[@type='submit']")
    def navigate_to(self, path="/login"):
        return super().navigate_to(path)
    def enter_username(self, username):
        self.send_keys(self.USERNAME_LOCATOR, username)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_LOCATOR, password)

    def click_login_button(self):
        self.click_element(self.LOGINBTN_LOCATOR)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        
    def get_username_value(self):
        return self.find_element(self.USERNAME_LOCATOR).get_attribute("value")

    def get_password_value(self):
        return self.find_element(self.PASSWORD_LOCATOR).get_attribute("value")