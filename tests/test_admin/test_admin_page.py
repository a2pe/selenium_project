import time

from selenium.webdriver.common.by import By


def test_admin_page_catalog(admin_page):
    """Тестирование количества подразделов в каталоге на странице администратора."""
    admin_page.fullscreen_window()
    time.sleep(3)
    admin_page.find_element(By.XPATH, '//*[@id="menu-catalog"]/a').click()
    time.sleep(3)
    catalog_all = admin_page.find_elements(By.XPATH, '//*[@id="collapse-1"]//li')
    # Берем количество подразделов, включая вложенные в Attributes.
    assert len(catalog_all) == 12, "Неверное количество подразделов в каталоге"


def test_admin_categories(admin_page):
    """Тестирование дефолтного значения элементов на странице Категорий в админской панели."""
    admin_page.find_element(By.LINK_TEXT, 'Dashboard').click()
    admin_page.fullscreen_window()
    time.sleep(3)
    admin_page.find_element(By.XPATH, '//*[@id="menu-catalog"]/a').click()
    admin_page.find_element(By.LINK_TEXT, "Categories").click()
    time.sleep(3)
    catalog_table = admin_page.find_elements(By.XPATH, '//*[@id="form-category"]/div[1]/table/tbody/tr')
    assert len(catalog_table) == 10, "Неверное количество элементов в таблице на странице Категорий"


def test_admin_categories_sorting(admin_page):
    """Тестирование категорий в каталоге при обратной сортировке."""
    admin_page.find_element(By.LINK_TEXT, 'Dashboard').click()
    admin_page.fullscreen_window()
    time.sleep(3)
    admin_page.find_element(By.XPATH, '//*[@id="menu-catalog"]/a').click()
    admin_page.find_element(By.LINK_TEXT, "Categories").click()
    time.sleep(3)
    admin_page.find_element(By.LINK_TEXT, 'Sort Order').click()
    admin_page.maximize_window()
    first_element = admin_page.find_element(By.XPATH, '//*[@id="form-category"]/div[1]/table/tbody/tr[1]/td[2]')
    assert first_element.text == 'MP3 Players\nEnabled'


def test_admin_notification_bell(admin_page):
    admin_page.find_element(By.LINK_TEXT, 'Dashboard').click()
    time.sleep(3)
    admin_page.find_element(By.XPATH, '//*[@id="nav-notification"]/a').click()
    element = admin_page.find_element(By.CSS_SELECTOR, '#nav-notification > div > span')
    assert element.text == "No results!"


# Тест проходит через раз(
#
def test_admin_settings(admin_page):
    """Тестирование очистки кеша в настройках в админской панели."""
    time.sleep(4)
    admin_page.find_element(By.LINK_TEXT, 'Dashboard').click()
    admin_page.find_element(By.CSS_SELECTOR, '#button-setting > i').click()
    admin_page.maximize_window()
    admin_page.find_element(By.XPATH, '//*[@id="modal-developer"]/div/div/div[2]/table/tbody/tr[1]/td[3]/button').click()
    time.sleep(3)
    alert_message = admin_page.find_element(By.XPATH, '//*[@id="alert"]/div').text
    assert alert_message == 'Success: You have cleared the Theme cache!'
