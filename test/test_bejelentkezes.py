import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from data_conduit import *
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

    def test_login(self):
        casual_registration(self.browser)
        casual_logout(self.browser)


        sign_in = self.browser.find_element_by_xpath('//a[@href="#/login"]')
        sign_in.click()

        email = self.browser.find_element_by_xpath('//input[@placeholder="Email"]')
        password = self.browser.find_element_by_xpath('//input[@placeholder="Password"]')
        uniq_name = "Angela1"
        email.send_keys(uniq_name + "@hotmail.com")
        pw = "Pepi1234!$"
        password.send_keys(pw)
        sign_in_button = self.browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        sign_in_button.click()
        # browser.switch_to.parent_frame()
        # WebDriverWait(browser, 5).until(alert_is_present())
        # popup = browser.switch_to.alert
        # message = popup.text
        # print(popup)

        time.sleep(2)

        success_login = self.browser.find_elements_by_xpath('//a[@class="nav-link"]')[2]
        assert success_login.text == uniq_name
        print(success_login.text)

        success_login_popup = self.browser.find_element_by_xpath('//div[@class="swal-text"]')
        # success_login_popup.click()
        popup = self.browser.switch_to.alert



        time.sleep(2)
        # browser.switch_to.parent_frame()
        # browser.switch_to.frame(success_login)
        # browser.switch_to.frame(success_login_popup)
        # time.sleep(2)
        assert success_login_popup.text == "Logging you in... Please wait..."
        print(success_login_popup.text)

