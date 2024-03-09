from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators


class TestLogout:
    def test_personal_account_logout(self, user):
        user.find_element(*Locators.PERSONAL_ACCOUNT).click()
        (WebDriverWait(user, 10).until(expected_conditions.element_to_be_clickable(Locators.LOGOUT_BUTTON)))
        user.find_element(*Locators.LOGOUT_BUTTON).click()
        (WebDriverWait(user, 10).until(expected_conditions.element_to_be_clickable(Locators.LOGIN_BUTTON_LOGIN_PAGE)))
        result = user.find_element(*Locators.LOGIN_BUTTON_LOGIN_PAGE).text
        assert result == "Войти", 'Ошибка при выходе из аккаунта'
