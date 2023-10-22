from selenium.webdriver.common.by import By

from selenium_project.page_objects.BasePage import BasePage


class CatalogPage(BasePage):
    DESKTOPS = (By.LINK_TEXT, "Desktops")
    DESKTOP_ITEMS = (By.XPATH, '//*[@id="narbar-menu"]/ul/li[1]/div/div/ul/li')
    SHOW_ALL_DESKTOPS = (By.LINK_TEXT, "Show All Desktops")
    DESKTOP_DESCRIPTION = (By.XPATH, '//*[@id="content"]/div[1]/div[2]/p')
    BUTTON_LIST = (By.ID, "button-list")
    BUTTON_GRID = (By.ID, "button-grid")
    PHONES_AND_PDAS = (By.LINK_TEXT, "Phones & PDAs")
    SORT = (By.ID, "input-sort")
    SORT_BY_MOST_EXPENSIVE = (By.XPATH, '//*[@id="input-sort"]/option[5]')
    PRICE = (By.XPATH, '//*[@id="product-list"]/div[1]/div/div[2]/div/div/span[1]')
    CAMERAS = (By.LINK_TEXT, 'Cameras')
    PRODUCTS = (By.XPATH, '//*[@id="product-list"]')
    ADD_TO_COMPARE_1 = (By.XPATH, '//*[@id="product-list"]/div[1]/div/div[2]/form/div/button[3]')
    ADD_TO_COMPARE_2 = (By.XPATH, '//*[@id="product-list"]/div[2]/div/div[2]/form/div/button[3]')
    COMPARE_TOTAL = (By.ID, 'compare-total')

    def select_desktops(self):
        self.click(self.element(self.DESKTOPS))

    def desktop_items(self):
        items = self.elements(self.DESKTOP_ITEMS)
        return items

    def show_all_desktops(self):
        self.click(self.element(self.SHOW_ALL_DESKTOPS))

    def show_desktop_description(self):
        description = self.element(self.DESKTOP_DESCRIPTION)
        return description

    def click_button_grid(self):
        self.click(self.element(self.BUTTON_GRID))

    def click_button_list(self):
        self.click(self.element(self.BUTTON_LIST))

    def click_phones_and_pdas(self):
        self.click(self.element(self.PHONES_AND_PDAS))

    def sort(self):
        self.click(self.element(self.SORT))

    def sort_by_most_expensive(self):
        self.click(self.element(self.SORT_BY_MOST_EXPENSIVE))

    def check_price(self):
        price = self.element(self.PRICE)
        return price

    def select_camera_items(self):
        self.click(self.element(self.CAMERAS))

    def add_to_compare_1_product(self):
        self.click(self.element(self.ADD_TO_COMPARE_1))

    def add_to_compare_2_product(self):
        self.click(self.element(self.ADD_TO_COMPARE_2))

    def compare_total(self):
        self.click(self.element(self.COMPARE_TOTAL))
