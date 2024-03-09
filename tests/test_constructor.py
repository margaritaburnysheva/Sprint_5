from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import Locators


class TestConstructor:
    def test_switch_to_buns_menu(self, driver):
        driver.find_element(*Locators.FILLING_TUB_CONSTRUCTOR).click()
        driver.find_element(*Locators.BUN_TUB_CONSTRUCTOR).click()
        (WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.BUN_MENU_TITLE)))
        result = driver.find_element(*Locators.BUN_TUB_CONSTRUCTOR).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in result, 'Ошибка при переходе к разделу "Булки"'

    def test_switch_to_sauces_menu(self, driver):
        driver.find_element(*Locators.SAUCE_TUB_CONSTRUCTOR).click()
        (WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.SAUCE_MENU_TITLE)))
        result = driver.find_element(*Locators.SAUCE_TUB_CONSTRUCTOR).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in result, 'Ошибка при переходе к разделу "Coycы"'

    def test_switch_to_fillings_menu(self, driver):
        driver.find_element(*Locators.FILLING_TUB_CONSTRUCTOR).click()
        (WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.FILLING_MENU_TITLE)))
        result = driver.find_element(*Locators.FILLING_TUB_CONSTRUCTOR).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in result, 'Ошибка при переходе к разделу "Начинки"'
