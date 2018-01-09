import unittest

import time
from selenium.webdriver import Chrome
from Test_Unit.facebook_POM import LoginPage
from selenium.webdriver.support.select import Select

class Test_Google(unittest.TestCase):
    def test_google_title(self):
        browser = Chrome("C:/Users/vpqs60/Downloads/chromedriver_win32/chromedriver.exe")
        browser.maximize_window()
        browser.implicitly_wait(30)
        browser.get("https://www.facebook.com")
        fb = LoginPage(browser)
        fb.wait_for_login_page_to_load()
        fb.user_first_name_textbox().send_keys("Raju")
        fb.user_last_name_textbox().send_keys("Kumar")
        fb.user_mobile_number_or_email_textbox().send_keys("rajukumar@gmail.com")
        fb.user_re_enter_email_textbox().send_keys("rajukumar@gmail.com")
        fb.user_new_password_textbox().send_keys("pwd123")
        time.sleep(1)
        Select(fb.user_birthday_day_dropdown()).select_by_index(7)
        Select(fb.user_birthday_month_dropdown()).select_by_index(5)
        Select(fb.user_birthday_year_dropdown()).select_by_value("2015")
        time.sleep(2)
        fb.user_male_radio_button().click()
        time.sleep(2)
        fb.user_create_button.click()
        #time.sleep(3)
        #fb.browser.close()

