import time
from selenium import webdriver
from data_conduit import *
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

## Test-007 a Global Feed lista bejárása a lapozógombokkal
class TestConduitListPagination(object):
    def setup(self):
        self.browser_options = Options()
        self.browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=self.browser_options)
        self.browser.get(URL)

    def teardown(self):
        self.browser.quit()

    def test_pagination(self):
        casual_login(self.browser)
        driver_wait(self.browser,'//a[@class="page-link"]')
        pages = self.browser.find_elements_by_xpath('//a[@class="page-link"]')

        for i in range(1, len(pages)):
            self.browser.find_elements_by_xpath('//a[@class="page-link"]')[i].click()

        page_button_color = self.browser.find_elements_by_xpath('//a[@class="page-link"]')[i].value_of_css_property('background-color')
        assert page_button_color == 'rgba(92, 184, 92, 1)'  # megváltozik a gomb színe: rgba(255, 255, 255, 1) lenne, ha nem lenne aktív

        casual_logout(self.browser)