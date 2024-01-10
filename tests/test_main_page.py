import random
import string
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.login_main_page import LoginMainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestMainPage(LoginMainPage):
    password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    login = password + "@inbox.ru"

    def test_main_page_nav_bar(self, browser, main_page):
        menu_items = browser.find_elements(By.CSS_SELECTOR, "ul.navbar-nav > li")
        assert len(menu_items) == 8, "Неверное количество элементов меню"

    def test_main_page_top_menu(self, browser, main_page):
        menu_items = browser.find_elements(By.CSS_SELECTOR, "div.float-end>ul>li")
        assert len(menu_items) == 5, "Неверное количество элементов меню"

    def test_seearch_success(self, browser, main_page):
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        browser.find_element(*LoginMainPage.SEARCH).send_keys("imac" + Keys.ENTER)
        expected_content = "Products meeting the search criteria"
        actual_result = wait.until(
            EC.visibility_of_element_located(LoginMainPage.SEARCH_RESULT)).text
        assert actual_result == expected_content, "Searching is failed"

    def test_search_failed(self, browser, main_page):
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        browser.find_element(*LoginMainPage.SEARCH).send_keys("RIMAC" + Keys.ENTER)
        expected_content = "There is no product that matches the search criteria."
        actual_result = wait.until(EC.visibility_of_element_located(LoginMainPage.SEARCH_FAILED)).text
        assert actual_result == expected_content
