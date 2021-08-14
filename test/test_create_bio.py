import time
from selenium import webdriver
from data_conduit import *
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

## Test-008 a felhasználó rövid bemutatkozásának létrehozása
class TestConduitCreateBio(object):
    def setup(self):
        self.browser_options = Options()
        self.browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=self.browser_options)
        self.browser.get(URL)

    def teardown(self):
        self.browser.quit()

    def test_createbio(self):
        casual_login(self.browser)
        time.sleep(4)

        settings = self.browser.find_elements_by_xpath('//a[@class="nav-link"]')[1].click()
        driver_wait(self.browser,'//textarea[@class="form-control form-control-lg"]')
        biography_field = self.browser.find_element_by_xpath('//textarea[@class="form-control form-control-lg"]')
        biography_field.clear()

        biography_field.send_keys(text_for_modification)

        update_settings_button = self.browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]').click()

        driver_wait(self.browser,'//button[@class="swal-button swal-button--confirm"]')
        confirm_button = self.browser.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]').click()

        home = self.browser.find_elements_by_xpath('//a[@class="nav-link"]')[0].click()
        time.sleep(1)
        settings = self.browser.find_elements_by_xpath('//a[@class="nav-link"]')[1].click()

        driver_wait(self.browser,'//textarea[@class="form-control form-control-lg"]')
        biography_field = self.browser.find_element_by_xpath('//textarea[@class="form-control form-control-lg"]').get_attribute("value")
        assert biography_field == text_for_modification

        casual_logout(self.browser)
