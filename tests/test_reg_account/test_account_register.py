import time

import pytest
from selenium.webdriver.common.by import By
from faker import Faker

fake = Faker()
NUM_OF_NEW_ACCOUNTS = 5


@pytest.mark.parametrize('email, name, lastname, password', [
    (fake.ascii_free_email(), fake.first_name(),
     fake.last_name(), fake.password()) for v in range(NUM_OF_NEW_ACCOUNTS)]
                         )
def test_register_new_account(browser, email, name, lastname, password):
    browser.get(browser.url + '/index.php?route=account/register')
    time.sleep(3)
    first_name = browser.find_element(By.CSS_SELECTOR, '#input-firstname')
    first_name.click()
    first_name.send_keys(name)
    last_name = browser.find_element(By.CSS_SELECTOR, '#input-lastname')
    last_name.click()
    last_name.send_keys(lastname)
    email_field = browser.find_element(By.CSS_SELECTOR, '#input-email')
    email_field.click()
    email_field.send_keys(email)
    password_field = browser.find_element(By.CSS_SELECTOR, '#input-password')
    password_field.click()
    password_field.send_keys(password)
    browser.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
    browser.find_element(By.XPATH, '//*[@id="form-register"]/div/div/input').click()
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(3)
    browser.find_element(By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[2]/div/a/span').click()
    browser.find_element(By.XPATH, '//*[@id="top"]/div/div[2]/ul/li[2]/div/ul/li[5]/a').click()
    time.sleep(3)
