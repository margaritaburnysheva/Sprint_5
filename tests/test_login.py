from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from constants import Constants
from locators import Locators


class TestLogin:
    def test_login_button_main_page(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*Locators.EMAIL_INPUT_FORM_LOGIN).send_keys(Constants.USER_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_FORM_LOGIN).send_keys(Constants.USER_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_LOGIN_PAGE).click()
        (WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON_MAIN_PAGE)))
        result = driver.find_element(*Locators.ORDER_BUTTON_MAIN_PAGE).text
        assert result == 'Оформить заказ', 'Ошибка при входе по кнопке «Войти в аккаунт» на главной'

    def test_login_personal_account_button_main_page(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.EMAIL_INPUT_FORM_LOGIN).send_keys(Constants.USER_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_FORM_LOGIN).send_keys(Constants.USER_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_LOGIN_PAGE).click()
        (WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON_MAIN_PAGE)))
        result = driver.find_element(*Locators.ORDER_BUTTON_MAIN_PAGE).text
        assert result == 'Оформить заказ', 'Ошибка при входе через кнопку «Личный кабинет»'

    def test_login_button_login_form_registration(self, driver):
        driver.get(Constants.REGISTRATION_URL)
        (WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_LOGIN_FORM_REGISTRATION)))
        driver.find_element(*Locators.BUTTON_LOGIN_FORM_REGISTRATION).click()
        driver.find_element(*Locators.EMAIL_INPUT_FORM_LOGIN).send_keys(Constants.USER_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_FORM_LOGIN).send_keys(Constants.USER_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_LOGIN_PAGE).click()
        (WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON_MAIN_PAGE)))
        result = driver.find_element(*Locators.ORDER_BUTTON_MAIN_PAGE).text
        assert result == 'Оформить заказ', 'Ошибка при входе через кнопку «Войти» в форме регистрации'

    def test_login_button_login_forgot_password_page(self, driver):
        driver.get(Constants.FORGOT_PASSWORD_URL)
        (WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_LOGIN_FORGOT_PASSWORD_FORM)))
        driver.find_element(*Locators.BUTTON_LOGIN_FORGOT_PASSWORD_FORM).click()
        driver.find_element(*Locators.EMAIL_INPUT_FORM_LOGIN).send_keys(Constants.USER_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_FORM_LOGIN).send_keys(Constants.USER_PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_LOGIN_PAGE).click()
        (WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON_MAIN_PAGE)))
        result = driver.find_element(*Locators.ORDER_BUTTON_MAIN_PAGE).text
        assert result == 'Оформить заказ', 'Ошибка при входе через кнопку «Войти» в форме восстановления пароля'
