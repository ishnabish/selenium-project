from selenium.webdriver.chrome.webdriver import WebDriver

driver: WebDriver = None


def setup_module():
    print('setup module started')
    global driver
    driver = WebDriver(executable_path='D://selenium//chromedriver.exe')
    driver.implicitly_wait(3)


def teardown_module():
    print('teardown module started')
    global driver
    driver.close()


def test_module_setup_driver():
    print('test invocation started')
    driver.get('http://2ch.hk')
    search_input = driver.find_element_by_xpath('//li[@href="/b/"]')
    search_input.click()

    import time
    time.sleep(3)
    assert True