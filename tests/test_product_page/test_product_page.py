import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def test_product_page_link(browser):
    """Тестирование наличия элементов на странице продукта."""
    browser.get(browser.url + '/en-gb/product/smartphone/iphone')
    # Clicking the link to access all Apple products.
    browser.find_element(By.LINK_TEXT, "Apple").click()
    # Finding the header for the Apple products.
    element_header = browser.find_element(By.XPATH, "/html/body/main/div[2]/div/div/h2")
    assert element_header.text == "Apple"


def test_adding_product_to_wishlist(browser):
    """Тестирование добавления товара в вишлист без предварительной регистрации."""
    browser.get(browser.url + 'en-gb/product/smartphone/htc-touch-hd')
    browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/form/div/button[1]').click()
    time.sleep(1)
    element = browser.find_element(By.ID, 'alert').text
    assert element == 'You must login or create an account to save HTC Touch HD to your wish list!'


def test_adding_product_to_cart(browser):
    """Тестирование добавления товара определенного цвета в корзину."""
    browser.get(browser.url + 'en-gb/product/cameras/canon-eos-5d')
    time.sleep(1)
    browser.find_element(By.XPATH, '//*[@id="input-option-226"]').click()
    browser.find_element(By.XPATH, '//*[@id="input-option-226"]/option[2]').click()
    time.sleep(1)
    browser.find_element(By.ID, 'button-cart').click()
    element = browser.find_element(By.ID, 'alert').text
    assert element == 'Success: You have added Canon EOS 5D to your shopping cart!'


def test_adding_product_to_cart_with_delivery(browser):
    """Тестирование добавления товара в корзину с выбором даты доставки."""
    browser.get(browser.url + 'en-gb/product/laptop-notebook/hp-lp3065')
    time.sleep(1)
    browser.find_element(By.ID, 'input-option-225').click()
    # wait = WebDriverWait(browser, 5)
    # wait.until(ec.visibility_of_element_located((By.CLASS_NAME, 'next available')))
    month_year_date = browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[2]').text
    while not (month_year_date.__eq__("Dec 2023")):
        browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[3]').click()
        month_year_date = browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[2]').text
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/tbody/tr[2]/td[2]').click()
    browser.find_element(By.ID, 'button-cart').click()
    wait = WebDriverWait(browser, 5)
    wait.until(ec.visibility_of_element_located((By.ID, 'alert')))
    element = browser.find_element(By.ID, 'alert').text
    assert element == 'Success: You have added HP LP3065 to your shopping cart!'


def test_adding_several_products_to_cart(browser):
    """Тестирование добавления нескольких товаров."""
    browser.get(browser.url + 'en-gb/product/mp3-players/ipod-classic')
    time.sleep(1)
    el = browser.find_element(By.ID, 'input-quantity')
    el.clear()
    el.send_keys('2')
    assert el.get_attribute('value') == '2'
    browser.find_element(By.ID, 'button-cart').click()
    wait = WebDriverWait(browser, 5)
    wait.until(ec.visibility_of_element_located((By.ID, 'alert')))
    element = browser.find_element(By.ID, 'alert').text
    assert element == 'Success: You have added iPod Classic to your shopping cart!'
