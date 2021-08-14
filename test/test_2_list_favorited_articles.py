import time
from selenium import webdriver
from data_conduit import *
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

## Test-006 a felhasználó kedvenc cikkeinek listázása
class TestConduitListFavoritedArticles(object):
    def setup(self):
        self.browser_options = Options()
        self.browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=self.browser_options)
        self.browser.get(URL)

    def teardown(self):
        self.browser.quit()

    def test_list_favorited_articles(self):
        casual_login(self.browser)
        time.sleep(2)

        for like in range(3):
            like_button = self.browser.find_elements_by_xpath('//i[@class="ion-heart"]')[like].click()
        driver_wait(self.browser,'//a[@class="preview-link"]')

        global_feed_list = []
        global_feed_articles = self.browser.find_elements_by_xpath('//a[@class="preview-link"]')
        for article in global_feed_articles[0:3]:
            global_feed_list.append(article.text)

        time.sleep(1)

        user_page = self.browser.find_elements_by_xpath('//a[@class="nav-link"]')[2].click()
        time.sleep(2)
        favorited_articles = self.browser.find_element_by_xpath('//a[@class="nav-link router-link-exact-active active"]').click()

        time.sleep(2)

        favorited_articles_list = []
        liked_articles = self.browser.find_elements_by_xpath('//a[@class="preview-link"]')
        for articles in liked_articles:
            favorited_articles_list.append(articles.text)

        assert favorited_articles_list == global_feed_list

        casual_logout(self.browser)