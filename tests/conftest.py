import pytest
from selenium import webdriver
from config.config import Config
from utils.browser_helper import get_driver

@pytest.fixture(scope="class")
def setup(request):
    driver = get_driver(Config.BROWSER)
    driver.maximize_window()
    driver.get(Config.BASE_URL)
    
    # Hapus cache berdasarkan browser
    if Config.BROWSER == "chrome":
        # Menghapus cache di Chrome
        driver.execute_cdp_cmd('Network.clearBrowserCache', {})
        driver.execute_cdp_cmd('Network.clearBrowserCookies', {})
    
    elif Config.BROWSER == "firefox":
        # Menghapus cache dan cookies di Firefox
        driver.delete_all_cookies()
        driver.execute_script("window.localStorage.clear();")
        driver.execute_script("window.sessionStorage.clear();")
    
    request.cls.driver = driver
    yield
    driver.quit()
