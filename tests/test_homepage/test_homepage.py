import time
import allure

from selenium.webdriver.common.by import By
from selenium_project.page_objects.MainPage import MainPage


@allure.epic('Epic #5')
@allure.feature('Home Page Main Functions')
@allure.story('Homepage Carousel')
@allure.title('Checking the link for the first element in the carousel')
def test_homepage_carousel(browser):
    """Тестирование ссылки на первый элемент в карусели на главной странице."""
    MainPage(browser).select_carousel()
    time.sleep(3)
    element_1 = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/ul[1]/li[1]')
    assert element_1.text == 'Product Code: SAM1'
    element_2 = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/ul[1]/li[2]')
    assert element_2.text == 'Reward Points: 1000'
    element_3 = browser.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/ul[1]/li[3]')
    assert element_3.text == 'Availability: Pre-Order'


@allure.epic('Epic #5')
@allure.feature('Home Page Main Functions')
@allure.story('Homepage Search')
@allure.title('Verifying the search results from the Home Page')
def test_homepage_search(browser):
    """Тестирования поиска товаров и отображения результатов с главной страницы."""
    MainPage(browser).main_search()
    MainPage(browser).click_search()
    time.sleep(4)
    product_number = MainPage(browser).product_elements()
    assert len(product_number) == 2


@allure.epic('Epic #5')
@allure.feature('Home Page Main Functions')
@allure.story('Homepage Currency Dropdown')
@allure.title('Checking the texts for each of the currencies from the dropdown')
def test_homepage_currency_dropdown(browser):
    """Тестирование дропдауна валют на главной странице"""
    MainPage(browser).click_currency_dropdown()
    time.sleep(4)
    currencies = MainPage(browser).currency_elements()
    assert len(currencies) == 3
    cur_1 = currencies[0].text
    assert cur_1 == '€ Euro'
    cur_2 = currencies[1].text
    assert cur_2 == '£ Pound Sterling'
    cur_3 = currencies[2].text
    assert cur_3 == '$ US Dollar'


@allure.epic('Epic #5')
@allure.feature('Home Page Main Functions')
@allure.story('Homepage Elements')
@allure.title('Checking the title for the first element on the Home Page')
def test_homepage_element(browser):
    """Проверка атрибута 'title' для первого элемента на главной странице."""
    browser.get(browser.url)
    pic = MainPage(browser).first_elem_on_page()
    assert pic.get_attribute('title') == 'MacBook'


@allure.epic('Epic #5')
@allure.feature('Home Page Main Functions')
@allure.story('Homepage Carousel')
@allure.title('Checking the title for the second element in the carousel')
def test_check_title_on_homepage(browser):
    """Тестирование ожидания элемента из карусели на главной странице."""
    browser.get(browser.url)
    elem = MainPage(browser).second_elem_in_carousel()
    assert elem.get_attribute('alt') == "MacBookAir"
