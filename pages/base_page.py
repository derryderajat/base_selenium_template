from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, Config.TIMEOUT)

    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)
    def navigate_to(self, path=""):
        self.driver.get(Config.BASE_URL + path)