import time
from selenium import webdriver
from data_conduit import *
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import csv

## Test-09 az articles.csv fájlból cikkek beolvasása és posztolása
class TestConduitAddArticlesCsv(object):
    def setup(self):
        self.browser_options = Options()
        self.browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=self.browser_options)
        self.browser.maximize_window()
        self.browser.get(URL)

    def teardown(self):
        self.browser.quit()

    def test_add_articles_csv(self):
        casual_login(self.browser)
        time.sleep(1)
        new_article_button = self.browser.find_elements_by_xpath('//a[@class="nav-link"]')[0].click()
        driver_wait(self.browser,'//input[@class="form-control form-control-lg"]')

        with open('test/articles.csv', 'r', encoding="utf-8") as art_file:
            art_table_reader = csv.reader(art_file, delimiter=';')
            new_articles_list = []
            for row in art_table_reader:
                if row[0] != 'Title':
                    new_articles_list.append(row[0])
                    i = 0
                    for i in range(4):
                        article_fields = self.browser.find_element_by_xpath(articles_fields_list[i])
                        article_fields.send_keys(row[i])
                    publish_button = self.browser.find_element_by_xpath('//button[@type="submit"]').click()
                    time.sleep(1)
                    new_article_button2 = self.browser.find_elements_by_xpath('//a[@class="nav-link"]')[1].click()
                    time.sleep(1)

        user_page = self.browser.find_elements_by_xpath('//a[@class="nav-link"]')[2].click()
        time.sleep(1)
        home = self.browser.find_elements_by_xpath('//a[@class="nav-link"]')[0]
        home.click()
        time.sleep(1)
        global_feed_list = []
        global_feed_articles = self.browser.find_elements_by_xpath('//div[@class="article-preview"]//a//h1')
        for article in global_feed_articles:
            global_feed_list.append(article.text)

        for i in range(len(new_articles_list)):
            assert new_articles_list[i] in global_feed_list

        casual_logout(self.browser)
