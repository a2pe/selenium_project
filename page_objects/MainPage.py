import allure
from selenium.webdriver.common.by import By

from selenium_project.page_objects.BasePage import BasePage


class MainPage(BasePage):
    CAROUSEL = (By.ID, "carousel-banner-0")
    SEARCH_FIELD = (By.NAME, "search")
    TO_SEARCH = 'Sam'  # to search for Samsung
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='button']")
    CURRENCY_DROPDOWN = (By.CLASS_NAME, "dropdown")
    CURRENCIES = (By.XPATH, '//*[@id="form-currency"]/div/ul/li')
    PRODUCT_ELEMENTS = (By.XPATH, '//*[@id="product-list"]/div')
    FIRST_ELEMENT_ON_PAGE = (By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[1]/a/img')
    SECOND_EL_IN_CAROUSEL = (By.CSS_SELECTOR, "#carousel-banner-0 > div.carousel-inner > div.carousel-item.active "
                                              "> div > div > img")

    @allure.step('Просмотр карусели')
    def select_carousel(self):
        self.click(self.element(self.CAROUSEL))

    @allure.step('Поиск товара в каталогах')
    def main_search(self):
        self._input(self.element(self.SEARCH_FIELD), self.TO_SEARCH)

    @allure.step('Выбор кнопки поиска')
    def click_search(self):
        self.click(self.element(self.SEARCH_BUTTON))

    @allure.step('Выбор дропдауна с доступными валютами')
    def click_currency_dropdown(self):
        self.click(self.element(self.CURRENCY_DROPDOWN))

    @allure.step('Возвращение списка с валютами')
    def currency_elements(self):
        currency_els = self.elements(self.CURRENCIES)
        return currency_els

    @allure.step('Список товаров по результатам поиска')
    def product_elements(self):
        product_elements = self.elements(self.PRODUCT_ELEMENTS)
        return product_elements

    @allure.step('Получение первого элемента на странице')
    def first_elem_on_page(self):
        el = self.element(self.FIRST_ELEMENT_ON_PAGE)
        return el

    @allure.step('Ожидание второго элемента в карусели на главной странице')
    def second_elem_in_carousel(self):
        el = self.element(self.SECOND_EL_IN_CAROUSEL)
        return el
