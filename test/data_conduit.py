def casual_registration(browser):
    sign_up = browser.find_element_by_xpath('//a[@href="#/register"]')
    sign_up.click()
    username = browser.find_element_by_xpath('//input[@placeholder="Username"]')
    email = browser.find_element_by_xpath('//input[@placeholder="Email"]')
    password = browser.find_element_by_xpath('//input[@placeholder="Password"]')
    username.send_keys("Angela1")
    email.send_keys("Angela1@hotmail.com")
    password.send_keys("Pepi1234!$")
    sign_up_button = browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    sign_up_button.click()


def casual_logout(browser):
    logout_button = browser.find_elements_by_xpath('//a[@class="nav-link"]')[3]
    logout_button.click()