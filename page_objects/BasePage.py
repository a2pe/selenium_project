import allure
from selenium.webdriver import ActionChains

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, wait=3):
        self.driver = driver
        self.wait = WebDriverWait(driver, wait)
        self.actions = ActionChains(driver)
        self.logger = driver.logger
        self.class_name = type(self).__name__

    @allure.step('Нажимаю на элемент: {element}')
    def click(self, element):
        self.logger.info('%s: Нажимаю на элемент: %s' % (self.class_name, element))
        ActionChains(self.driver).move_to_element(element).pause(0.1).click().perform()

    @allure.step('Ввожу {value} в элемент: {element}')
    def _input(self, element, value):
        self.logger.info('%s: Ввожу "%s" в поле элемента: %s' % (self.class_name, value, element))
        self.click(element)
        element.clear()
        element.send_keys(value)

    # @allure.step
    # def element_in_element(self, parent_locator: tuple, child_locator: tuple):
    #     return self.element(parent_locator).find_element(*child_locator)

    @allure.step
    def element(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.logger.error('На странице не отображается элемент %s' % locator)
            allure.attach(
                name=f'{self.driver.current_url}',
                body=self.driver.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Не дождался видимости элемента {locator}")

    @allure.step
    def elements(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            self.logger.error('На странице не отображаются элементы %s' % locator)
            allure.attach(
                name=f'{self.driver.current_url}',
                body=self.driver.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError(f"Не дождался видимости элементов {locator}")

    @allure.step
    def wait_and_accept_alert(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present(), 'Timed out waiting for alert')
            alert = self.driver.switch_to.alert
            alert.accept()
        except TimeoutException:
            self.logger.error('На странице не появился алерт.')
            allure.attach(
                name=f'{self.driver.current_url}',
                body=self.driver.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
            raise AssertionError('На странице не появился алерт.')
