import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class TestConduitRegistration(object):
    def setup(self):
        self.browser_options = Options()
        self.browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=self.browser_options)
        self.browser.get("http://localhost:1667")

    def teardown(self):
        self.browser.quit()


    def test_registration(self):
        sign_up = self.browser.find_element_by_xpath('//a[@href="#/register"]')
        sign_up.click()

        username = self.browser.find_element_by_xpath('//input[@placeholder="Username"]')
        email = self.browser.find_element_by_xpath('//input[@placeholder="Email"]')
        password = self.browser.find_element_by_xpath('//input[@placeholder="Password"]')
        uniq_name = "Pepi" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")).replace('-', '').replace('_', '')
        print(uniq_name)
        username.send_keys(uniq_name)
        email.send_keys(uniq_name + "@hotmail.com")
        pw = "Pepi1234!$"
        password.send_keys(pw)
        sign_up_button = self.browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        sign_up_button.click()

        time.sleep(4)
        success = self.browser.find_element_by_xpath('//*[@class="swal-text"]')
        assert success.text == "Your registration was successful!"

