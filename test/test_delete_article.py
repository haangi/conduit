import time
from selenium import webdriver
from data_conduit import *
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

## Test-11 a shopping.txt fájlból létrehoz egy cikket, majd törli a posztok közül ##
class TestConduitDeleteArticle(object):
    def setup(self):
        self.browser_options = Options()
        self.browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=self.browser_options)
        self.browser.maximize_window()
        self.browser.get(URL)

    def teardown(self):
        self.browser.quit()

    def test_delete_article(self):
        casual_login(self.browser)
        time.sleep(1)
        new_article_button = self.browser.find_elements_by_xpath('//a[@class="nav-link"]')[0].click()
        time.sleep(1)
        with open('test/shopping.txt', 'r', encoding="utf-8") as news_file:
            i = 0
            for i in range(4):
                news = news_file.readline()
                news = news.strip('\n')
                if i == 0:
                    delete_title = news
                field = self.browser.find_element_by_xpath(articles_fields_list[i])
                field.send_keys(news)
        publish_button = self.browser.find_element_by_xpath('//button[@type="submit"]').click()
        driver_wait(self.browser,'//i[@class="ion-trash-a"]')
        delete_button = self.browser.find_element_by_xpath('//i[@class="ion-trash-a"]').click()
        driver_wait(self.browser,'//div[@class="article-preview"]//a//h1')

        global_feed_list = []
        global_feed_articles = self.browser.find_elements_by_xpath('//div[@class="article-preview"]//a//h1')
        for article in global_feed_articles:
            global_feed_list.append(article.text)
        result = delete_title in global_feed_list
        assert result == False

        casual_logout(self.browser)