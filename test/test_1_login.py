import time

from selenium import webdriver
from data_conduit import *
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

## Test-003 regisztrált felhasználó belépése
class TestConduitLogin(object):
    def setup(self):
        self.browser_options = Options()
        self.browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=self.browser_options)
        self.browser.get(URL)

    def teardown(self):
        self.browser.quit()

    def test_login(self):
        casual_registration(self.browser)
        time.sleep(1)
        casual_logout(self.browser)
        driver_wait(self.browser, '//a[@href="#/login"]')
        sign_in = self.browser.find_element_by_xpath('//a[@href="#/login"]').click()
        driver_wait(self.browser, '//input[@placeholder="Email"]')
        email = self.browser.find_element_by_xpath('//input[@placeholder="Email"]')
        password = self.browser.find_element_by_xpath('//input[@placeholder="Password"]')
        email.send_keys(uniq_name + "@hotmail.com")
        password.send_keys(pw)
        sign_in_button = self.browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]').click()
        time.sleep(1)
        success_login = self.browser.find_elements_by_xpath('//a[@class="nav-link"]')[2]
        assert success_login.text == uniq_name
        casual_logout(self.browser)

