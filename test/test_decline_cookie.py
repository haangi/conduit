import time
from selenium import webdriver
from data_conduit import URL
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Test-005 cookie kezelés elutasítása
class TestConduitCookieDecline(object):
    def setup(self):
        self.browser_options = Options()
        self.browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=self.browser_options)
        self.browser.get(URL)

    def teardown(self):
        self.browser.quit()

    def test_declinecookie(self):
        decline_button = self.browser.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[1]/div').click()
        time.sleep(1)
        decline_cookie = self.browser.get_cookie('vue-cookie-accept-decline-cookie-policy-panel')
        assert decline_cookie['value'] == 'decline'
