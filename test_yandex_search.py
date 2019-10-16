from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


def test_yandex_search():
    driver = WebDriver(executable_path='D://selenium//chromedriver.exe')
    driver.get('https://www.ya.ru')
    search_input = driver.find_element_by_xpath('//input[@id="text"]')
    search_input.send_keys('market.yandex.ru')
    search_button = driver.find_element_by_xpath('//div[@class="search2__button"]//button[@type="submit"]')
    search_button.click()

    def check_results_count(driver):
        inner_search_results = driver.find_elements_by_xpath('//li[@class="serp-item"]')
        return len(inner_search_results) > 10

    WebDriverWait(driver, 5, 0.5).until(check_results_count)

    search_results = driver.find_elements_by_xpath('//li[@class="serp-item"]')
    link = search_results[0].find_element_by_xpath('.//h2/a')
    link.click()

    driver.switch_to.window(driver.window_handles[1])

    assert driver.title == 'Рейтинг интернет-проектов по данным Яндекса. Самые популярные ресурсы в разных тематиках и кросс-девайсная статистика посещаемости.'
