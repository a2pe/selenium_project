import time

from selenium.webdriver.common.by import By
from selenium_project.page_objects.CatalogPage import CatalogPage
from selenium_project.page_objects.MainPage import MainPage


def test_catalog_desktop_dropdown(browser):
    """Тестирование наличия элементов на странице каталога в разделе Desktops."""
    CatalogPage(browser).select_desktops()
    desktops_items = CatalogPage(browser).desktop_items()
    assert len(desktops_items) == 2
    assert desktops_items[0].text == 'PC (0)'
    assert desktops_items[1].text == 'Mac (1)'


def test_catalog_show_desktops(browser):
    """Тестирование описания на странице каталога при выборе всех Desktops."""
    browser.get(browser.url)
    CatalogPage(browser).select_desktops()
    CatalogPage(browser).show_all_desktops()
    desktops_description = CatalogPage(browser).show_desktop_description()
    assert desktops_description.text == 'Example of category description text'


def test_catalog_show_products_by_grid_or_list(browser):
    """Тестирование отображения товаров в каталоге и сортировки по цене."""
    browser.get(browser.url)
    CatalogPage(browser).click_phones_and_pdas()
    CatalogPage(browser).click_button_list()
    time.sleep(2)
    CatalogPage(browser).click_button_grid()
    time.sleep(2)
    CatalogPage(browser).sort()
    # --- По какой-то причине не работает такой вариант, ошибка ElementNotInteractableException
    # CatalogPage(browser).sort_by_most_expensive()
    browser.find_element(By.XPATH, '//*[@id="input-sort"]/option[5]').click()
    first_element = CatalogPage(browser).check_price()
    assert first_element.text == '$337.99'

    # Замена текущей валюты с доллара на евро
    MainPage(browser).click_currency_dropdown()
    time.sleep(1)
    currencies = MainPage(browser).currency_elements()
    currencies[0].click()
    time.sleep(1)
    first_element_price = CatalogPage(browser).check_price()
    assert first_element_price.text == '302.92€'


def test_catalog_show_products_by_grid(browser):
    """Тестирование отображения товаров в каталоге и сортировки по цене."""
    CatalogPage(browser).select_camera_items()
    CatalogPage(browser).add_to_compare_1_product()
    CatalogPage(browser).add_to_compare_2_product()
    CatalogPage(browser).compare_total()
    time.sleep(3)
    elems = browser.find_elements(By.XPATH, '//*[@id="content"]/table/tbody[1]/tr[1]/td')
    assert len(elems) == 3
