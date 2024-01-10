import time

from pages.login_admin_page import LoginAdminPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestAdminPage(LoginAdminPage):

    def test_login_logout_admin(self, browser, admin_login):
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        wait.until(EC.title_is("Dashboard"))  # Дождались заголовок Dashboard

        browser.find_element(*LoginAdminPage.PERSON_LABEL)  # видим Лого Администратора
        browser.find_element(*LoginAdminPage.BUTTON_LOGOUT)  # видим кнопку разлогина
        assert_percent = "Счетчик процентов работает некорректно! Значение превышает 100%"
        # Проверки корректности
        percent_orders = wait.until(
            EC.visibility_of_element_located(LoginAdminPage.PERCENT_ORDERS)).text
        assert "100%" >= percent_orders >= "0%", assert_percent

        percent_sales = wait.until(
            EC.visibility_of_element_located(LoginAdminPage.PERCENT_SALES)).text
        assert "100%" >= percent_sales >= "0%", assert_percent

        percent_customers = wait.until(
            EC.visibility_of_element_located(LoginAdminPage.PERCENT_CUSTOMERS)).text
        assert "100%" >= percent_customers >= "0%", assert_percent
        # Логаут из авдминки с проверкой
        browser.find_element(*LoginAdminPage.BUTTON_LOGOUT).click()
        # time.sleep(3)
        excp_header_card = "Please enter your login details."
        act_header_card = wait.until(
            EC.visibility_of_element_located(LoginAdminPage.LOGIN_FORM)).text
        assert act_header_card == excp_header_card, "No such card authorization"

    def test_incorrect_password_login(self, browser):
        wait = WebDriverWait(browser, 5, poll_frequency=1)
        browser.get(browser.url + "/administration")
        browser.find_element(*LoginAdminPage.USERNAME_INPUT).send_keys("user")
        browser.find_element(*LoginAdminPage.PASSWORD_INPUT).send_keys("incorrect")
        browser.find_element(*LoginAdminPage.SUBMIT_BUTTON).submit()

        wait.until(EC.visibility_of_element_located(LoginAdminPage.UNSUCCESSIBLE_LOGIN_ALERT))
        message = browser.find_element(*LoginAdminPage.UNSUCCESSIBLE_LOGIN_ALERT).text
        assert_message = "No match for Username and/or Password."
        assert message == assert_message, "Некорректное сообщение об ошибке"

