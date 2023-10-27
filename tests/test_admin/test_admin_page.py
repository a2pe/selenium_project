import time
import allure

import pytest
from faker import Faker
from selenium.webdriver.common.by import By
from selenium_project.page_objects.AdminPage import AdminPage
from selenium_project.page_objects.ProductPage import ProductPage

fake = Faker()
NUM_OF_NEW_PRODUCTS = 5


@allure.epic('Epic #1')
@allure.feature('Admin Page Catalog')
@allure.story('Checking the Admin Page Catalog Subsections')
@allure.title('Listing the catalog subsections')
def test_admin_page_catalog(admin_page):
    """Тестирование количества подразделов в каталоге на странице администратора."""
    AdminPage(admin_page).click_catalog()
    catalog_all = AdminPage(admin_page).catalog_elements()
    assert len(catalog_all) == 10, "Неверное количество подразделов в каталоге"


@allure.epic('Epic #1')
@allure.feature('Admin Page Catalog')
@allure.story('Checking the Admin Page Catalog Categories')
@allure.title('Checking the number of default elements in the table in the Category')
def test_admin_categories(admin_page):
    """Тестирование дефолтного значения элементов на странице Категорий в админской панели."""
    AdminPage(admin_page).navigate_to_dashboard()
    AdminPage(admin_page).click_catalog()
    AdminPage(admin_page).select_categories()
    catalog_table = admin_page.find_elements(By.XPATH, '//*[@id="form-category"]/div[1]/table/tbody/tr')
    assert len(catalog_table) == 10, "Неверное количество элементов в таблице на странице Категорий"


@allure.epic('Epic #1')
@allure.feature('Admin Page Catalog')
@allure.story('Checking the Admin Page Catalog Categories')
@allure.title('Listing the Categories with reverse sorting')
def test_admin_categories_sorting(admin_page):
    """Тестирование категорий в каталоге при обратной сортировке."""
    AdminPage(admin_page).navigate_to_dashboard()
    AdminPage(admin_page).click_catalog()
    AdminPage(admin_page).select_categories()
    AdminPage(admin_page).sort_order()
    admin_page.maximize_window()
    first_element = admin_page.find_element(By.XPATH, '//*[@id="form-category"]/div[1]/table/tbody/tr[1]/td[2]')
    assert first_element.text == 'MP3 Players\nEnabled', "Неверное название категории при обратной сортировке."


@allure.epic('Epic #2')
@allure.feature('Admin Page Notifications')
@allure.title('Checking the default notification message.')
def test_admin_notification_bell(admin_page):
    """Тестирование уведомлений в админской панели."""
    AdminPage(admin_page).navigate_to_dashboard()
    AdminPage(admin_page).click_notification()
    element = AdminPage(admin_page).check_notification_text().text
    assert element == "No results!"


@allure.epic('Epic #2')
@allure.feature('Admin Page Settings')
@allure.title('Checking clearing cache from the Settings option on the Admin Page.')
def test_admin_settings(admin_page):
    """Тестирование очистки кеша в настройках в админской панели."""
    AdminPage(admin_page).navigate_to_dashboard()
    AdminPage(admin_page).click_setting_icon()
    admin_page.maximize_window()
    admin_page.find_element(By.XPATH,
                            '//*[@id="modal-developer"]/div/div/div[2]/table/tbody/tr[1]/td[3]/button').click()
    time.sleep(3)
    alert_message = ProductPage(admin_page).get_alert().text
    time.sleep(3)
    assert alert_message == 'Success: You have cleared the Theme cache!'


@allure.epic('Epic #3')
@allure.feature('Admin Page - Product Operations')
@allure.title('Adding a new product from the Categories > Products on the Admin Page.')
@pytest.mark.parametrize('product, meta_tag, model, keyword', [
    (fake.word(), fake.word(),
     fake.word(), fake.word()) for v in range(NUM_OF_NEW_PRODUCTS)]
                         )
def test_add_new_product(admin_page, product, meta_tag, model, keyword):
    """Тестирование добавления продукта из админской панели."""
    AdminPage(admin_page).navigate_to_dashboard()
    AdminPage(admin_page).click_catalog()
    AdminPage(admin_page).select_categories()
    AdminPage(admin_page).select_products()
    AdminPage(admin_page).click_add_option()
    time.sleep(3)
    AdminPage(admin_page).add_product(product, meta_tag, model, keyword)
    time.sleep(3)
    AdminPage(admin_page).submit_button()
    time.sleep(3)
    alert = ProductPage(admin_page).get_alert().text
    assert alert == 'Success: You have modified products!'


@allure.epic('Epic #3')
@allure.feature('Admin Page - Product Operations')
@allure.title('Deleting a product from the Categories > Products on the Admin Page.')
def test_delete_product(admin_page):
    """Тестирование удаления продукта из админской панели."""
    AdminPage(admin_page).navigate_to_dashboard()
    AdminPage(admin_page).click_catalog()
    AdminPage(admin_page).select_products()
    AdminPage(admin_page).click_price()
    AdminPage(admin_page).click_price()
    admin_page.maximize_window()
    AdminPage(admin_page).check_first_product()
    AdminPage(admin_page).delete_product()
    time.sleep(3)
    AdminPage(admin_page).wait_and_accept_alert()
    time.sleep(3)
    alert = ProductPage(admin_page).get_alert().text
    assert alert == 'Success: You have modified products!'
