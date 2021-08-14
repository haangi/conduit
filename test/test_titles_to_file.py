from selenium import webdriver
from data_conduit import *
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

## Test-12 a Conduit oldalon posztolt összes cikk címeinek titles.txt fájlba írása ##
class TestConduitTitlestoFile(object):
    def setup(self):
        self.browser_options = Options()
        self.browser_options.headless = True
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=self.browser_options)
        self.browser.get(URL)

    def teardown(self):
        self.browser.quit()

    def test_titles_to_file(self):
        casual_login(self.browser)

        driver_wait(self.browser,'//div[@class="article-preview"]//a//h1')

        global_feed_list = []
        global_feed_articles = self.browser.find_elements_by_xpath('//div[@class="article-preview"]//a//h1')
        for article in global_feed_articles:
            global_feed_list.append(article.text)

        with open('test/titles.txt', 'w', encoding="utf-8") as title_file:
            for i in range(len(global_feed_list)):
                title_file.write(global_feed_list[i] + '\n')

        with open('test/titles.txt', 'r', encoding="utf-8") as reading:
            reading_title_list = reading.read().splitlines()  # leveszi az entert a sorok végéről

        assert global_feed_list == reading_title_list

        casual_logout(self.browser)