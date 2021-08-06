from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

URL = "http://localhost:1667"

class TestConduit(object):
    def setup(self):
        self.browser_options = Options()
        self.browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=self.browser_options)
        self.browser.maximize_window()
        self.browser.get(URL)

    def teardown(self):
        self.browser.quit()

    # # Test1
    def test_home_page_appearance(self):
        webpage = self.browser.title
        assert webpage == "Conduit"


