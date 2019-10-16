import time

from selenium.webdriver.chrome.webdriver import WebD


def test_conftest(driver: WebDriver):
    print('start test_conftest method')
    driver.get('http://google.com')
    time.sleep(3)
    print('stop test_conftest method')


def test_conftest_2(driver: WebDriver):
    print('start test_conftest_2 method')
    driver.get('http://ya.ru')
    time.sleep(3)
    print('stop test_conftest_2 method')