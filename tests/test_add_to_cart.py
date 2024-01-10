import random
import string
import time

from selenium.webdriver import Keys
from pages.login_main_page import LoginMainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestMainPage(LoginMainPage):
    password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    login = password + "@inbox.ru"

    def test_add_to_cart(self, browser, main_login):
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        browser.get(browser.url + "/en-gb?route=checkout/cart")
        time.sleep(1)
        while True:
            try:
                browser.find_element(*LoginMainPage.REMOVE_POSITION).click()
            except Exception:
                break
        browser.find_element(*LoginMainPage.SEARCH).send_keys("imac" + Keys.ENTER)
        expected_content = "Products meeting the search criteria"
        actual_result = wait.until(
            EC.presence_of_element_located(LoginMainPage.SEARCH_RESULT)).text
        assert actual_result == expected_content, "Searching is failed"
        browser.execute_script("window.scrollTo(0, 300)")
        time.sleep(1)
        browser.find_element(*LoginMainPage.ADD_TO_CART_FIRST_ITEM).click()

        wait.until(
            EC.presence_of_element_located(LoginMainPage.CLOSE_ALERT))
        browser.find_element(*LoginMainPage.CLOSE_ALERT).click()

        browser.get(browser.url + "/en-gb?route=checkout/cart")
        time.sleep(4)
        product_name = browser.find_element(*LoginMainPage.PRODUCT_NAME).text
        model = browser.find_element(*LoginMainPage.MODEL).text
        quantity = int(browser.find_element(*LoginMainPage.QUANTITY).get_attribute('value'))
        assert product_name == "iMac", "Не тот товар"
        assert model == "Product 14", "Не та модель товара"
        assert quantity == 1, "Разъехалось количество товаров в корзине"
