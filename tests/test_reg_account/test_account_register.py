import time
import allure

import pytest
from faker import Faker
from selenium_project.page_objects.AccountRegPage import AccountRegPage

fake = Faker()
NUM_OF_NEW_ACCOUNTS = 5


@allure.epic('Epic #7')
@allure.feature('Account Registration')
@allure.story('Account Creation')
@allure.title('Creating account with all checks and subscriptions')
@pytest.mark.parametrize('email, name, lastname, password', [
    (fake.ascii_free_email(), fake.first_name(),
     fake.last_name(), fake.password()) for v in range(NUM_OF_NEW_ACCOUNTS)]
                         )
def test_register_new_account(browser, email, name, lastname, password):
    browser.get(browser.url + '/index.php?route=account/register')
    time.sleep(3)
    AccountRegPage(browser).enter_first_name(name)
    AccountRegPage(browser).enter_last_name(lastname)
    AccountRegPage(browser).enter_email(email)
    AccountRegPage(browser).enter_password(password)
    AccountRegPage(browser).check_subscribe()
    AccountRegPage(browser).check_privacy_policy()
    AccountRegPage(browser).click_submit_button()
    AccountRegPage(browser).logout()
    AccountRegPage(browser).register()
