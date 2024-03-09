import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import Locators


class TestRegistration:
    def test_success_registration(self, driver, fake_name, fake_email, fake_password):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.LINK_REGISTRATION).click()
        driver.find_element(*Locators.NAME_INPUT_FORM_REGISTRATION).send_keys(fake_name)
        driver.find_element(*Locators.EMAIL_INPUT_FORM_REGISTRATION).send_keys(fake_email)
        driver.find_element(*Locators.PASSWORD_INPUT_FORM_REGISTRATION).send_keys(fake_password)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        (WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_BUTTON_LOGIN_PAGE)))
        driver.find_element(*Locators.EMAIL_INPUT_FORM_LOGIN).send_keys(fake_email)
        driver.find_element(*Locators.PASSWORD_INPUT_FORM_LOGIN).send_keys(fake_password)
        driver.find_element(*Locators.LOGIN_BUTTON_LOGIN_PAGE).click()
        (WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON_MAIN_PAGE)))
        result = driver.find_element(*Locators.ORDER_BUTTON_MAIN_PAGE).text
        assert result == 'Оформить заказ', 'Ошибка регистрации пользователя'

    def test_fail_registration_with_empty_name(self, driver, fake_email, fake_password):
        name = ''
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.LINK_REGISTRATION).click()
        driver.find_element(*Locators.NAME_INPUT_FORM_REGISTRATION).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT_FORM_REGISTRATION).send_keys(fake_email)
        driver.find_element(*Locators.PASSWORD_INPUT_FORM_REGISTRATION).send_keys(fake_password)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        result = driver.find_element(*Locators.BUTTON_REGISTRATION).text
        assert result == 'Зарегистрироваться', 'Не работает проверка на наличие символов в поле "Имя"'

    @pytest.mark.parametrize('email',  ['', 'testtesttest123@yandex', '1234567', '@@@@'])
    def test_fail_registration_with_invalid_email(self, email, driver, fake_name, fake_password):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.LINK_REGISTRATION).click()
        driver.find_element(*Locators.NAME_INPUT_FORM_REGISTRATION).send_keys(fake_name)
        driver.find_element(*Locators.EMAIL_INPUT_FORM_REGISTRATION).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT_FORM_REGISTRATION).send_keys(fake_password)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        result = driver.find_element(*Locators.BUTTON_REGISTRATION).text
        assert result == 'Зарегистрироваться', 'Не работает проверка формата email'

    @pytest.mark.parametrize('password', ['1', 'aa1', '@@@@a'])
    def test_fail_registration_with_invalid_password(self, password, driver, fake_name, fake_email):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.LINK_REGISTRATION).click()
        driver.find_element(*Locators.NAME_INPUT_FORM_REGISTRATION).send_keys(fake_name)
        driver.find_element(*Locators.EMAIL_INPUT_FORM_REGISTRATION).send_keys(fake_email)
        driver.find_element(*Locators.PASSWORD_INPUT_FORM_REGISTRATION).send_keys(password)
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        result = driver.find_element(*Locators.PASSWORD_ERROR_MESSAGE).text
        assert result == 'Некорректный пароль', 'Не работает проверка при некорректном пароле'
