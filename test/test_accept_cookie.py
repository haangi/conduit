import time
from selenium import webdriver
from data_conduit import URL
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Test-004 cookie kezelés elfogadása
class TestConduitCookieAccept(object):
    def setup(self):
        self.browser_options = Options()
        self.browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=self.browser_options)
        self.browser.get(URL)

    def teardown(self):
        self.browser.quit()

    def test_acceptcookie(self):
        accept_button = self.browser.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div').click()
        time.sleep(1)
        accept_cookie = self.browser.get_cookie('vue-cookie-accept-decline-cookie-policy-panel')
        assert accept_cookie['value'] == 'accept'

