from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

def get_driver(browser_name="chrome"):
    if browser_name == "chrome":
        service = ChromeService()
        options = webdriver.ChromeOptions()
        return webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        service = FirefoxService()
        options = webdriver.FirefoxOptions()
        return webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Browser {browser_name} is not supported.")
