import time
import allure

from selenium.webdriver.common.by import By
from selenium_project.page_objects.ProductPage import ProductPage


@allure.epic('Epic #6')
@allure.feature('Product Page Main Functions')
@allure.story('Product Page links')
@allure.title('Verifying the link from the product page')
def test_product_page_link(browser):
    """Тестирование наличия элементов на странице продукта."""
    browser.get(browser.url + '/en-gb/product/smartphone/iphone')
    ProductPage(browser).click_apple_link()
    element_header = ProductPage(browser).check_product_title()
    assert element_header.text == "Apple"


@allure.epic('Epic #6')
@allure.feature('Product Page Main Functions')
@allure.story('Product Page Wishlist')
@allure.title('Verifying adding the product to the wishlist with no prior registration')
def test_adding_product_to_wishlist(browser):
    """Тестирование добавления товара в вишлист без предварительной регистрации."""
    browser.get(browser.url + 'en-gb/product/smartphone/htc-touch-hd')
    ProductPage(browser).add_to_wish_list()
    element = ProductPage(browser).get_alert().text
    assert element == 'You must login or create an account to save HTC Touch HD to your wish list!'


@allure.epic('Epic #6')
@allure.feature('Product Page Main Functions')
@allure.story('Product Page Cart')
@allure.title('Verifying adding the product of a specific color to the cart')
def test_adding_product_to_cart(browser):
    """Тестирование добавления товара определенного цвета в корзину."""
    browser.get(browser.url + 'en-gb/product/cameras/canon-eos-5d')
    ProductPage(browser).select_color()
    browser.find_element(By.XPATH, '//*[@id="input-option-226"]/option[2]').click()
    ProductPage(browser).add_to_cart()
    element = ProductPage(browser).get_alert().text
    assert element == 'Success: You have added Canon EOS 5D to your shopping cart!'


@allure.epic('Epic #6')
@allure.feature('Product Page Main Functions')
@allure.story('Product Page Cart')
@allure.title('Verifying adding the product with the delivery date to the cart')
def test_adding_product_to_cart_with_delivery(browser):
    """Тестирование добавления товара в корзину с выбором даты доставки."""
    browser.get(browser.url + 'en-gb/product/laptop-notebook/hp-lp3065')
    time.sleep(1)
    ProductPage(browser).select_date()
    month_year_date = ProductPage(browser).default_date().text
    while not (month_year_date.__eq__("Dec 2023")):
        browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/thead/tr[1]/th[3]').click()
        month_year_date = ProductPage(browser).default_date().text
    browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/table/tbody/tr[2]/td[2]').click()
    ProductPage(browser).add_to_cart()
    element = ProductPage(browser).get_alert().text
    assert element == 'Success: You have added HP LP3065 to your shopping cart!'


@allure.epic('Epic #6')
@allure.feature('Product Page Main Functions')
@allure.story('Product Page Cart')
@allure.title('Verifying adding several products to the cart')
def test_adding_several_products_to_cart(browser):
    """Тестирование добавления нескольких товаров."""
    browser.get(browser.url + 'en-gb/product/mp3-players/ipod-classic')
    el = ProductPage(browser).add_quantity()
    assert el.get_attribute('value') == '2'
    ProductPage(browser).add_to_cart()
    element = ProductPage(browser).get_alert().text
    assert element == 'Success: You have added iPod Classic to your shopping cart!'
