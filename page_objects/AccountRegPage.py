import time
import allure

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

    @allure.step('Ввод имени')
    def enter_first_name(self, name):
        self._input(self.element(self.FIRST_NAME), name)

    @allure.step('Ввод фамилии')
    def enter_last_name(self, lastname):
        self._input(self.element(self.LAST_NAME), lastname)

    @allure.step('Ввод почты')
    def enter_email(self, email):
        self._input(self.element(self.EMAIL_FIELD), email)

    @allure.step('Ввод пароля')
    def enter_password(self, password):
        self._input(self.element(self.PASSWORD_FIELD), password)

    @allure.step('Выбор подписки')
    def check_subscribe(self):
        self.click(self.element(self.SUBSCRIBE))

    @allure.step('Проставление чека напротив политики приватности')
    def check_privacy_policy(self):
        self.click(self.element(self.PRIVACY_POLICY))

    @allure.step('Отправка данных')
    def click_submit_button(self):
        self.click(self.element(self.SUBMIT))
        time.sleep(1)

    @allure.step('Выход из системы под текущим пользователем')
    def logout(self):
        self.click(self.element(self.LOGOUT))
        time.sleep(1)

    @allure.step('Регистрация')
    def register(self):
        self.click(self.element(self.REGISTER))
        time.sleep(1)
