import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker

from constants import Constants
from locators import Locators


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(Constants.BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def user(driver):
    driver.get(Constants.LOGIN_URL)
    driver.find_element(*Locators.EMAIL_INPUT_FORM_LOGIN).send_keys(Constants.USER_EMAIL)
    driver.find_element(*Locators.PASSWORD_INPUT_FORM_LOGIN).send_keys(Constants.USER_PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON_LOGIN_PAGE).click()
    (WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON_MAIN_PAGE)))
    return driver

@pytest.fixture(scope="function")
def fake_name():
    faker = Faker()
    name = faker.name()
    return name

@pytest.fixture(scope="function")
def fake_email():
    faker = Faker()
    email = faker.email()
    return email

@pytest.fixture(scope="function")
def fake_password():
    faker = Faker()
    password = faker.password(7)
    return password
