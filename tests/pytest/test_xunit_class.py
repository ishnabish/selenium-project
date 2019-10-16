import time

from selenium.webdriver.chrome.webdriver import WebDriver


class TestXUnitClass:
    driver: WebDriver

    def setup_method(self):
        print('setup method invocation')
        self.driver = WebDriver(executable_path='D://selenium//chromedriver.exe')
        self.driver.implicitly_wait(3)

    def teardown_method(self):
        print('teardown method invocation')
        self.driver.close()

    def test_xunit_class(self):
        print('test method invocation')
        self.driver.get('http://google.com')
        time.sleep(3)
        assert True

    def test_xunit_class_2(self):
        print('test method2 invocation')
        self.driver.get('http://ya.ru')
        time.sleep(3)
        assert True
