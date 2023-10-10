import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_homepage_carousel(browser):
    """Тестирование ссылки на первый элемент в карусели на главной странице."""
    browser.get(browser.url)
    browser.find_element(By.ID, "carousel-banner-0").click()
    time.sleep(3)
    element_1 = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/ul[1]/li[1]')
    assert element_1.text == 'Product Code: SAM1'
    element_2 = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/ul[1]/li[2]')
    assert element_2.text == 'Reward Points: 1000'
    element_3 = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/ul[1]/li[3]')
    assert element_3.text == 'Availability: Pre-Order'


def test_homepage_search(browser):
    """Тестирования поиска товаров и отображения результатов с главной страницы."""
    browser.get(browser.url)
    search_field = browser.find_element(By.NAME, "search")
    search_field.send_keys('Sam')
    browser.find_element(By.CSS_SELECTOR, "button[type='button']").click()
    time.sleep(4)
    product_number = browser.find_elements(By.XPATH, '//*[@id="product-list"]/div')
    assert len(product_number) == 2


def test_homepage_currency_dropdown(browser):
    """Тестирование дропдауна валют на главной странице"""
    browser.get(browser.url)
    browser.find_element(By.CLASS_NAME, "dropdown").click()
    time.sleep(4)
    currencies = browser.find_elements(By.XPATH, '//*[@id="form-currency"]/div/ul/li')
    assert len(currencies) == 3
    cur_1 = browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[1]')
    assert cur_1.text == '€ Euro'
    cur_2 = browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[2]')
    assert cur_2.text == '£ Pound Sterling'
    cur_3 = browser.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[3]')
    assert cur_3.text == '$ US Dollar'


def test_homepage_element(browser):
    """Проверка атрибута 'title' для первого элемента на главной странице."""
    browser.get(browser.url)
    pic = browser.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[1]/a/img')
    assert pic.get_attribute('title') == 'MacBook'


def test_check_title_on_homepage(browser):
    """Тестирование ожидания элемента из карусели на главной странице."""
    browser.get(browser.url)
    wait = WebDriverWait(browser, 10)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,
                                                 "#carousel-banner-0 > "
                                                 "div.carousel-inner > "
                                                 "div.carousel-item.active "
                                                 "> div > div > img")
                                                ), message='')
    elem = browser.find_element(By.CSS_SELECTOR, "#carousel-banner-0 > div.carousel-inner > "
                                                 "div.carousel-item.active "
                                                 "> div > div > img")
    assert elem.get_attribute('alt') == "MacBookAir"
