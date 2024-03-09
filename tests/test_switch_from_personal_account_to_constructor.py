from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators


class TestSwitchFromPersonalAccount:
    def test_switch_from_personal_account_click_constructor(self, user):
        user.find_element(*Locators.PERSONAL_ACCOUNT).click()
        (WebDriverWait(user, 10).until(expected_conditions.element_to_be_clickable(Locators.LOGOUT_BUTTON)))
        user.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        result = user.find_element(*Locators.ORDER_BUTTON_MAIN_PAGE).text
        assert result == 'Оформить заказ', 'Ошибка при переходе из Личного кабинета по клику на "Конструктор"'

    def test_switch_from_personal_account_click_logo(self, user):
        user.find_element(*Locators.PERSONAL_ACCOUNT).click()
        (WebDriverWait(user, 10).until(expected_conditions.element_to_be_clickable(Locators.LOGOUT_BUTTON)))
        user.find_element(*Locators.LOGO).click()
        result = user.find_element(*Locators.ORDER_BUTTON_MAIN_PAGE).text
        assert result == 'Оформить заказ', 'Ошибка при переходе из Личного кабинета по клику на логотип Stellar Burgers'
