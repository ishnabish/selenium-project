import pytest
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture
def driver(request):
    print('start fixture')
    chrome_driver = WebDriver(executable_path='D://selenium//chromedriver.exe')
    chrome_driver.implicitly_wait(3)
    yield chrome_driver
    print('stop fixture')
    chrome_driver.close()
