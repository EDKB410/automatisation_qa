import random
import string
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.login_main_page import LoginMainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCurrency(LoginMainPage):
    def test_main_page_currency(self, browser, main_page):
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        browser.find_element(*LoginMainPage.CURRENCY_DROPDOWN).click()
        browser.find_element(*LoginMainPage.SELECT_EUR).click()
        eur_price_macbook = wait.until(
            EC.visibility_of_element_located(LoginMainPage.PRICE_MAC_BOOK)).text
        assert eur_price_macbook == "472.33€", "Стоимость некорректна"

        browser.find_element(*LoginMainPage.CURRENCY_DROPDOWN).click()
        browser.find_element(*LoginMainPage.SELECT_GBP).click()
        gbr_price_macbook = wait.until(
            EC.visibility_of_element_located(LoginMainPage.PRICE_MAC_BOOK)).text
        assert gbr_price_macbook == "£368.73", "Стоимость некорректна"

        browser.find_element(*LoginMainPage.CURRENCY_DROPDOWN).click()
        browser.find_element(*LoginMainPage.SELECT_USD).click()
        usd_price_macbook = wait.until(
            EC.visibility_of_element_located(LoginMainPage.PRICE_MAC_BOOK)).text
        assert usd_price_macbook == "$602.00", "Стоимость некорректна"

    def test_catalog_page_currency(self, browser, main_page):
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        browser.get(browser.url + "/en-gb/catalog/desktops")
        browser.find_element(*LoginMainPage.CURRENCY_DROPDOWN).click()
        browser.find_element(*LoginMainPage.SELECT_EUR).click()
        eur_price_macbook = wait.until(
            EC.visibility_of_element_located(LoginMainPage.PRICE_MAC_BOOK)).text
        assert eur_price_macbook == "472.33€", "Стоимость некорректна"

        browser.find_element(*LoginMainPage.CURRENCY_DROPDOWN).click()
        browser.find_element(*LoginMainPage.SELECT_GBP).click()
        gbr_price_macbook = wait.until(
            EC.visibility_of_element_located(LoginMainPage.PRICE_MAC_BOOK)).text
        assert gbr_price_macbook == "£368.73", "Стоимость некорректна"

        browser.find_element(*LoginMainPage.CURRENCY_DROPDOWN).click()
        browser.find_element(*LoginMainPage.SELECT_USD).click()
        usd_price_macbook = wait.until(
            EC.visibility_of_element_located(LoginMainPage.PRICE_MAC_BOOK)).text
        assert usd_price_macbook == "$602.00", "Стоимость некорректна"