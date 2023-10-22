import time

from selenium.webdriver.common.by import By
from selenium_project.page_objects.BasePage import BasePage


class AdminPage(BasePage):
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    USERNAME = (By.CSS_SELECTOR, "#input-username")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    ADMIN_PASSWORD = 'bitnami'
    ADMIN_USERNAME = 'user'

    MENU_CATALOG = (By.XPATH, '//*[@id="menu-catalog"]/a')
    SUB_CATALOG = (By.XPATH, '//*[@id="collapse-1"]/li')

    DASHBOARD = (By.LINK_TEXT, 'Dashboard')
    CATEGORIES = (By.LINK_TEXT, "Categories")
    PRODUCTS = (By.LINK_TEXT, 'Products')

    SORT_OPTION = (By.LINK_TEXT, 'Sort Order')
    NOTIFICATION_BELL = (By.XPATH, '//*[@id="nav-notification"]/a')
    NOTIFICATION_INFO = (By.CSS_SELECTOR, '#nav-notification > div > span')
    SETTING_ICON = (By.CSS_SELECTOR, '#button-setting > i')

    ADD_OPTION = (By.XPATH, '//*[@id="content"]/div[1]/div/div/a')

    PRODUCT_FIELD = (By.ID, "input-name-1")
    META_TAG = (By.ID, "input-meta-title-1")
    DATA_TAB = (By.LINK_TEXT, 'Data')
    MODEL_FIELD = (By.ID, "input-model")
    SEO_TAB = (By.LINK_TEXT, 'SEO')
    SEO_KEYWORD = (By.ID, 'input-keyword-0-1')

    PRICE_SORT = (By.LINK_TEXT, 'Price')
    FIRST_PRODUCT_CHECK = (By.XPATH, '//*[@id="form-product"]/div[1]/table/tbody/tr[1]/td[1]/input')
    DELETE_OPTION = (By.XPATH, '//*[@id="content"]/div[1]/div/div/button[3]')

    def enter_password(self, password=ADMIN_PASSWORD):
        self._input(self.element(self.PASSWORD), password)

    def enter_username(self, username=ADMIN_USERNAME):
        self._input(self.element(self.USERNAME), username)

    def submit_button(self):
        self.click(self.element(self.SUBMIT_BUTTON))

    def click_catalog(self):
        self.click(self.element(self.MENU_CATALOG))

    def catalog_elements(self):
        return self.elements(self.SUB_CATALOG)

    def navigate_to_dashboard(self):
        self.click(self.element(self.DASHBOARD))

    def select_categories(self):
        self.click(self.element(self.CATEGORIES))

    def sort_order(self):
        self.click(self.element(self.SORT_OPTION))

    def click_notification(self):
        self.click(self.element(self.NOTIFICATION_BELL))

    def check_notification_text(self):
        return self.element(self.NOTIFICATION_INFO)

    def click_setting_icon(self):
        self.click(self.element(self.SETTING_ICON))
        time.sleep(3)

    def select_products(self):
        self.click(self.element(self.PRODUCTS))

    def click_add_option(self):
        self.click(self.element(self.ADD_OPTION))

    def add_product(self, product, meta_tag, model, keyword):
        self._input(self.element(self.PRODUCT_FIELD), product)
        self._input(self.element(self.META_TAG), meta_tag)
        self.click(self.element(self.DATA_TAB))
        self._input(self.element(self.MODEL_FIELD), model)
        self.click(self.element(self.SEO_TAB))
        self._input(self.element(self.SEO_KEYWORD), keyword)

    def click_price(self):
        self.click(self.element(self.PRICE_SORT))

    def check_first_product(self):
        self.click(self.element(self.FIRST_PRODUCT_CHECK))

    def delete_product(self):
        self.click(self.element(self.DELETE_OPTION))
