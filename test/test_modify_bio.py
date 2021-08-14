import time
from selenium import webdriver
from data_conduit import *
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

## Test-10 a felhasználó rövid bemutatkozásának a módosítása ##
class TestConduitModifyBio(object):
    def setup(self):
        self.browser_options = Options()
        self.browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=self.browser_options)
        self.browser.maximize_window()
        self.browser.get(URL)

    def teardown(self):
        self.browser.quit()

    def test_modifybio(self):
        casual_login(self.browser)
        time.sleep(1)
        casual_createbio(self.browser)
        driver_wait(self.browser,'//textarea[@class="form-control form-control-lg"]')

        new_bio = " ".join((text_for_modification, new_text_for_modification))

        biography_field = self.browser.find_element_by_xpath('//textarea[@class="form-control form-control-lg"]')
        biography_field.clear()
        biography_field.send_keys(new_bio)

        driver_wait(self.browser,'//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        update_settings_button = self.browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
        update_settings_button.click()

        driver_wait(self.browser,'//button[@class="swal-button swal-button--confirm"]')
        confirm_button = self.browser.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]')
        confirm_button.click()

        biography_field = self.browser.find_element_by_xpath('//textarea[@class="form-control form-control-lg"]').get_attribute("value")
        assert biography_field == new_bio

        casual_logout(self.browser)