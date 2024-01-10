import time
import random
import string

import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_admin_page import LoginAdminPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions

from selenium.webdriver.safari.service import Service as SafariService
from selenium.webdriver.safari.options import Options as SafariOptions

from pages.login_main_page import LoginMainPage


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser", default="chrome")
    url = request.config.getoption("--url", default="http://192.168.1.64:8081")

    if browser_name == "chrome":
        service = ChromeService()
        options = ChromeOptions()
        options.add_argument("headless=new")  # Отключение визуализации браузера
        driver = webdriver.Chrome(service=service, options=options)

    elif browser_name == "firefox":
        service = FFService()
        options = FFOptions()
        options.add_argument("-headless")  # Отключение визуализации браузера
        driver = webdriver.Firefox(service=service, options=options)

    else:
        service = SafariService()
        options = SafariOptions()
        options.add_argument("-headless")  # Отключение визуализации браузера
        driver = webdriver.Safari(service=service, options=options)

    # Set window size
    # width = 1920  # in pixels
    # height = 1080  # in pixels
    # driver.set_window_size(width, height)
    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver


@pytest.fixture()
def admin_login(browser):
    browser.get(browser.url + "/administration")
    browser.find_element(*LoginAdminPage.USERNAME_INPUT).send_keys("user")
    browser.find_element(*LoginAdminPage.PASSWORD_INPUT).send_keys("bitnami")
    browser.find_element(*LoginAdminPage.SUBMIT_BUTTON).submit()

@pytest.fixture()
def main_login(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 5, poll_frequency=1)
    wait.until(EC.title_is("Your Store"))
    browser.find_element(*LoginMainPage.ACCOUNT_DROPDOWN).click()
    browser.find_element(*LoginMainPage.LOGIN).click()
    browser.find_element(*LoginMainPage.EMAIL).send_keys("um8mp@inbox.ru")
    browser.find_element(*LoginMainPage.PASSWORD).send_keys("um8mp")
    browser.find_element(*LoginMainPage.CONTINUE_BUTTON).click()
    wait.until(
        EC.visibility_of_element_located(LoginMainPage.LOGIN_PAGE))


@pytest.fixture()
def main_page(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 5, poll_frequency=1)
    wait.until(EC.title_is("Your Store"))
