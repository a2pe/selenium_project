import pytest
import logging
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.safari.service import Service as SafariService


# def pytest_addoption(parser):
    # parser.addoption("--browser", action="store", default="chrome")
    # parser.addoption("--url", action="store", default="http://localhost/")
    # parser.addoption("--log_level", action="store", default="INFO")
    # parser.addoption("--executor", action="store", default="127.0.0.1")


log_map = {
    "INFO": logging.INFO,
    "DEBUG": logging.DEBUG,
    "WARNING": logging.WARNING,
}


@pytest.fixture(scope='session')
def browser(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")
    # executor = request.config.getoption("--executor")

    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f'logs/{request.node.name}.log', 'a+')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(log_map[log_level])

    logger.info("====> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    # To execute tests on a remote browser using selenoid.
    # executor_url = f"http://{executor}:4444/wd/hub"
    # options = webdriver.ChromeOptions()
    # caps = {
    #     "browserName": browser_name,
    #     "acceptInsecureCerts": True,
    # }
    #
    # for k, v in caps.items():
    #     options.set_capability(k, v)
    #
    # driver = webdriver.Remote(
    #     command_executor=executor_url,
    #     options=options
    # )

    if browser_name == "chrome":
        service = ChromiumService()
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        service = FFService()
        driver = webdriver.Firefox(service=service)
    elif browser_name == 'safari':
        service = SafariService()
        driver = webdriver.Safari(service=service)
    else:
        service = ChromiumService()
        driver = webdriver.Chrome(service=service)

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name
    logger.info('Browser %s started' % browser_name)

    def fin():
        driver.quit()
        logger.info("Test %s is finished at %s " % (request.node.name, datetime.datetime.now()))

    driver.get(url)
    driver.url = url

    request.addfinalizer(fin)
    return driver
