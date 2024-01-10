import random
import string

from pages.login_main_page import LoginMainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestMainPage(LoginMainPage):
    password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    login = password + "@inbox.ru"

    def test_register_new_account(self, browser, main_page):
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        browser.find_element(*LoginMainPage.ACCOUNT_DROPDOWN).click()
        browser.find_element(*LoginMainPage.REGISTER).click()
        browser.find_element(*LoginMainPage.FIRSTNAME).send_keys(f"solovev_{self.password}")
        browser.find_element(*LoginMainPage.LASTNAME).send_keys(f"evgeny_{self.password}")
        browser.find_element(*LoginMainPage.EMAIL).send_keys(self.login)
        browser.find_element(*LoginMainPage.PASSWORD).send_keys(self.password)
        browser.find_element(*LoginMainPage.PRIVACY_POLICY_CHECKBOX).click()
        browser.find_element(*LoginMainPage.CONTINUE_BUTTON).click()
        expected_content = "Your Account Has Been Created!"
        actual_result = wait.until(
            EC.visibility_of_element_located(LoginMainPage.CONGRAT_MESS)).text
        assert actual_result == expected_content, "You are not register"

    def test_login_logout(self, browser, main_login):
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        expected_content = "My Account"
        actual_result = wait.until(
            EC.visibility_of_element_located(LoginMainPage.LOGIN_PAGE)).text
        assert actual_result == expected_content, "You are not login"
        browser.find_element(*LoginMainPage.ACCOUNT_DROPDOWN).click()
        browser.find_element(*LoginMainPage.LOGOUT).click()
        expected_content = "Account Logout"
        actual_result = wait.until(
            EC.visibility_of_element_located(LoginMainPage.LOGOUT_PAGE)).text
        assert actual_result == expected_content, "You are not logout"
