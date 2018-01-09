from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage():
    def __init__(self,browser):
        self.browser = browser
    def wait_for_login_page_to_load(self):
        wait = WebDriverWait(self.browser, 30)
        wait.until(expected_conditions.visibility_of(self.browser.find_element_by_id("globalContainer")))
    def user_first_name_textbox(self):
        try:
            element = self.browser.find_element_by_id("u_0_l")
            return element
        except:
               return None
    def user_last_name_textbox(self):
        try:
            return self.browser.find_element_by_id("u_0_n")
        except:
            return None
    def user_mobile_number_or_email_textbox(self):
        try:
            return self.browser.find_element_by_id("u_0_q")
        except:
            return None
    def user_re_enter_email_textbox(self):
        try:
            return self.browser.find_element_by_id("u_0_t")
        except:
            return None
    def user_new_password_textbox(self):
        try:
            return self.browser.find_element_by_id("u_0_x")
        except:
            return None
    def user_birthday_day_dropdown(self):
        try:
            day = self.browser.find_element_by_id("day")
            return day
        except:
            return None
    def user_birthday_month_dropdown(self):
        try:
            month = self.browser.find_element_by_id("month")
            return month
        except:
            return None
    def user_birthday_year_dropdown(self):
        try:
            year = self.browser.find_element_by_id("year")
            return year
        except:
            return None
    def user_female_radio_button(self):
        try:
            return self.browser.find_element_by_id("u_0_b")
        except:
            return None
    def user_male_radio_button(self):
        try:
            return self.browser.find_element_by_id("u_0_c")
        except:
            return None
    @property
    def user_create_button(self):
        try:
            return self.browser.find_element_by_id("u_0_13")
            #return self.browser.find_element_by_xpath("//font[contains(text(),'Create account')]")
        except:
            return None