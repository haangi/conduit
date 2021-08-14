import time
from selenium import webdriver
from data_conduit import *
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

## Test-13 a Conduit oldalon a felhasználó kiléptetése az alkalmazásból ##
class TestConduitLogout(object):
    def setup(self):
        self.browser_options = Options()
        self.browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=self.browser_options)
        self.browser.get(URL)

    def teardown(self):
        self.browser.quit()

    def test_logout(self):
        casual_login(self.browser)
        time.sleep(1)
        logout_button = self.browser.find_elements_by_xpath('//a[@class="nav-link"]')[3]
        logout_button.click()
        driver_wait(self.browser,'//a[@href="#/login"]')
        sign_in = self.browser.find_element_by_xpath('//a[@href="#/login"]')
        assert sign_in.text == "Sign in"
