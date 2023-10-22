import time

from selenium.webdriver.common.by import By

from selenium_project.page_objects.BasePage import BasePage


class AccountRegPage(BasePage):

    FIRST_NAME = (By.CSS_SELECTOR, '#input-firstname')
    LAST_NAME = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#input-email')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#input-password')

    SUBSCRIBE = (By.CSS_SELECTOR, "input[type='checkbox']")
    PRIVACY_POLICY = (By.XPATH, '//*[@id="form-register"]/div/div/input')
    SUBMIT = (By.CSS_SELECTOR, "button[type='submit']")
    LOGOUT = (By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[2]/div/a/span')
    REGISTER = (By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[2]/div/ul/li[5]/a')

    def enter_first_name(self, name):
        self._input(self.element(self.FIRST_NAME), name)

    def enter_last_name(self, lastname):
        self._input(self.element(self.LAST_NAME), lastname)

    def enter_email(self, email):
        self._input(self.element(self.EMAIL_FIELD), email)

    def enter_password(self, password):
        self._input(self.element(self.PASSWORD_FIELD), password)

    def check_subscribe(self):
        self.click(self.element(self.SUBSCRIBE))

    def check_privacy_policy(self):
        self.click(self.element(self.PRIVACY_POLICY))

    def click_submit_button(self):
        self.click(self.element(self.SUBMIT))
        time.sleep(1)

    def logout(self):
        self.click(self.element(self.LOGOUT))
        time.sleep(1)

    def register(self):
        self.click(self.element(self.REGISTER))
        time.sleep(1)
