from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators


class TestSwitchToPersonalAccount:
    def test_switch_to_personal_account_on_click(self, user):
        user.find_element(*Locators.PERSONAL_ACCOUNT).click()
        (WebDriverWait(user, 10).until(expected_conditions.element_to_be_clickable(Locators.LOGOUT_BUTTON)))
        result = user.find_element(*Locators.LOGOUT_BUTTON).text
        assert result == 'Выход', 'Ошибка при переходе по клику на "Личный кабинет"'
