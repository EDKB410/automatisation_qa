from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_main_page import LoginMainPage


class TestCardProduct(LoginMainPage):

    def test_card_product_title(self, browser, main_page):
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        browser.get(browser.url + "/en-gb/product/desktops/canon-eos-5d")
        product_title = wait.until(
             EC.visibility_of_element_located(LoginMainPage.CARD_CANON_TITLE)).text
        assert product_title == "Canon EOS 5D", "Некорректное наименование товара"

    def test_card_product_price(self, browser, main_page):
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        browser.get(browser.url + "/en-gb/product/desktops/canon-eos-5d")
        product_price = wait.until(
            EC.visibility_of_element_located(LoginMainPage.PRICE_PRODUCT)).text
        assert product_price == "$98.00", "Некорректная стоимость товара"

    def test_card_product_add_to_card(self, browser, main_page):
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        browser.get(browser.url + "/en-gb/product/desktops/canon-eos-5d")
        browser.find_element(*LoginMainPage.REQUIRED_OPTION_SELECT).click()
        browser.find_element(*LoginMainPage.ADD_TO_CART_BUTTON).click()
        wait.until(
            EC.presence_of_element_located(LoginMainPage.CLOSE_ALERT))
        browser.find_element(*LoginMainPage.CLOSE_ALERT).click()

        browser.get(browser.url + "/en-gb?route=checkout/cart")
        product_name = wait.until(
            EC.visibility_of_element_located(LoginMainPage.PRODUCT_NAME)).text
        assert product_name == "Canon EOS 5D", "Некорректное наименование товара в корзине после добавления"
        model = browser.find_element(*LoginMainPage.MODEL).text
        assert model == "Product 3", "Не та модель товара"
        unit_price = browser.find_element(*LoginMainPage.UNIT_PRICE).text
        assert unit_price == "$98.00", "Некорректная стоимость товара"