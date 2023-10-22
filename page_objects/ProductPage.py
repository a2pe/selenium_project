import time

from selenium.webdriver.common.by import By

from selenium_project.page_objects.BasePage import BasePage


class ProductPage(BasePage):
    WISH_LIST = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/form/div/button[1]')
    COMPARE = (By.CSS_SELECTOR, "[data-original-title='Compare this Product']")
    CART = (By.CSS_SELECTOR, "#button-cart")
    APPLE_LINK = (By.LINK_TEXT, "Apple")
    CONTENT = (By.CSS_SELECTOR, '#content > h2')
    ALERT = (By.ID, 'alert')
    CAMERA_COLOR = (By.XPATH, '//*[@id="input-option-226"]')
    CAMERA_COLOR_RED = (By.XPATH, '//*[@id="input-option-226"]/option[1]')
    CAMERA_COLOR_BLUE = (By.XPATH, '//*[@id="input-option-226"]/option[2]')
    DATE_SELECTOR = (By.ID, 'input-option-225')
    DEFAULT_DATE = (By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[2]')
    INPUT_QUANTITY = (By.ID, 'input-quantity')

    def add_to_wish_list(self):
        self.click(self.element(self.WISH_LIST))

    def add_to_cart(self):
        time.sleep(2)
        self.click(self.element(self.CART))

    def click_apple_link(self):
        self.click(self.element(self.APPLE_LINK))

    def check_product_title(self):
        return self.element(self.CONTENT)

    def get_alert(self):
        time.sleep(2)
        return self.element(self.ALERT)

    def select_color(self):
        self.click(self.element(self.CAMERA_COLOR))

    def select_date(self):
        self.click(self.element(self.DATE_SELECTOR))

    def default_date(self):
        return self.element(self.DEFAULT_DATE)

    def add_quantity(self):
        self._input(self.element(self.INPUT_QUANTITY), '2')
        return self.element(self.INPUT_QUANTITY)
