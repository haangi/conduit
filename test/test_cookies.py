from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class TestConduitCookies(object):
    def setup(self):
        self.browser_options = Options()
        self.browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=self.browser_options)
        self.browser.get("http://localhost:1667")

    def teardown(self):
        self.browser.quit()

    def test_cookies(self):
        accept_button = self.browser.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div')
        assert self.browser.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[2]/div') != True
        assert self.browser.find_element_by_xpath('//*[@id="cookie-policy-panel"]/div/div[2]/button[1]/div') != True
        accept_button.click()
