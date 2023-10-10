import time

from selenium.webdriver.common.by import By


def test_catalog_desktop_dropdown(browser):
    """Тестирование наличия элементов на странице каталога в разделе Desktops."""
    browser.get(browser.url)
    browser.find_element(By.LINK_TEXT, "Desktops").click()
    desktops_items = browser.find_elements(By.XPATH, '//*[@id="narbar-menu"]/ul/li[1]/div/div/ul/li')
    assert len(desktops_items) == 2
    assert desktops_items[0].text == 'PC (0)'
    assert desktops_items[1].text == 'Mac (1)'


def test_catalog_show_desktops(browser):
    """Тестирование описания на странице каталога при выборе всех Desktops."""
    browser.get(browser.url)
    browser.find_element(By.LINK_TEXT, "Desktops").click()
    browser.find_element(By.LINK_TEXT, "Show All Desktops").click()
    desktops_description = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/p')
    assert desktops_description.text == 'Example of category description text'


def test_catalog_show_products_by_grid_or_list(browser):
    """Тестирование отображения товаров в каталоге и сортировки по цене."""
    browser.get(browser.url)
    browser.find_element(By.LINK_TEXT, "Phones & PDAs").click()
    browser.find_element(By.ID, "button-list").click()
    time.sleep(3)
    browser.find_element(By.ID, "button-grid").click()
    time.sleep(3)
    browser.find_element(By.XPATH, '//*[@id="input-sort"]/option[5]').click()
    first_element = browser.find_element(By.XPATH, '//*[@id="product-list"]/div[1]/div/div[2]/div/div/span[1]')
    assert first_element.text == '$337.99'

    # Замена текущей валюты с доллара на евро
    browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/a/span').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[1]/a').click()
    time.sleep(1)
    browser.maximize_window()
    first_element = browser.find_element(By.XPATH, '//*[@id="product-list"]/div[1]/div/div[2]/div/div/span[1]')
    assert first_element.text == '302.92€'


def test_catalog_show_products_by_grid(browser):
    """Тестирование отображения товаров в каталоге и сортировки по цене."""
    browser.get(browser.url)
    browser.find_element(By.LINK_TEXT, 'Cameras').click()
    browser.find_element(By.XPATH, '//*[@id="product-list"]/div[1]/div/div[2]/form/div/button[3]').click()
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="product-list"]/div[2]/div/div[2]/form/div/button[3]').click()
    time.sleep(1)
    browser.find_element(By.ID, 'compare-total').click()
    time.sleep(3)
    elems = browser.find_elements(By.XPATH, '//*[@id="content"]/table/tbody[1]/tr[1]/td')
    assert len(elems) == 3
