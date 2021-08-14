import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

## -----------------------------------------------------------------------------------##
URL = "http://localhost:1667"

articles_fields_list = ['//input[@class="form-control form-control-lg"]', '//input[@class="form-control"]',
                        '//textarea[@class="form-control"]', '//input[@class="ti-new-tag-input ti-valid"]']

text_for_modification = "Pepi vagyok. 36 éves és nagyon szeretek kirándulni."
new_text_for_modification = "Sokszor túrázom a hegyekben."

uniq_name = "Angela"            # regisztrációnál egyedi felhasználónevet hoz létre (github futás miatt kiszedve)
pw = "Pepi1234!$"

## -----------------------------------------------------------------------------------##
def driver_wait(browser,path):
    return WebDriverWait(browser, 5).until(EC.visibility_of_any_elements_located((By.XPATH, path)))

def casual_registration(browser):
    sign_up = browser.find_element_by_xpath('//a[@href="#/register"]')
    sign_up.click()
    time.sleep(1)
    username = browser.find_element_by_xpath('//input[@placeholder="Username"]')
    email = browser.find_element_by_xpath('//input[@placeholder="Email"]')
    password = browser.find_element_by_xpath('//input[@placeholder="Password"]')
    username.send_keys(uniq_name)
    email.send_keys(uniq_name + "@hotmail.com")
    password.send_keys(pw)
    sign_up_button = browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    sign_up_button.click()

def casual_login(browser):
    sign_in = browser.find_element_by_xpath('//a[@href="#/login"]')
    sign_in.click()
    email = browser.find_element_by_xpath('//input[@placeholder="Email"]')
    password = browser.find_element_by_xpath('//input[@placeholder="Password"]')
    email.send_keys(uniq_name + "@hotmail.com")
    password.send_keys(pw)
    sign_in_button = browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    sign_in_button.click()

def casual_createbio(browser):
    settings = browser.find_elements_by_xpath('//a[@class="nav-link"]')[1]
    settings.click()
    time.sleep(2)
    biography_field = browser.find_element_by_xpath('//textarea[@class="form-control form-control-lg"]')
    biography_field.clear()
    text_for_modification = "Pepi vagyok. 36 éves és nagyon szeretek kirándulni."
    biography_field.send_keys(text_for_modification)

    update_settings_button = browser.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    update_settings_button.click()
    time.sleep(2)
    confirm_button = browser.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]')
    confirm_button.click()

def casual_logout(browser):
    logout_button = browser.find_elements_by_xpath('//a[@class="nav-link"]')[3]
    logout_button.click()