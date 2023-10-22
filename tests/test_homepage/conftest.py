import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.safari.service import Service as SafariService
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://localhost/")


@pytest.fixture(scope='session')
def browser(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    if browser_name == "chrome":
        service = ChromiumService()
        driver = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        service = FFService()
        driver = webdriver.Firefox(service=service)
    elif browser_name == 'safari':
        service = SafariService()
        driver = webdriver.Safari(service=service)
    else:
        service = ChromiumService()
        driver = webdriver.Chrome(service=service)

    driver.get(url)
    driver.url = url

    yield driver

    driver.close()
