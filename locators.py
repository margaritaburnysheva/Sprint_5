from selenium.webdriver.common.by import By


class Locators:
    #локаторы на главной странице (до авторизации)
    LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, '//*[contains(@class,"button_button_size_large")]') #кнопка "Войти в аккаунт" на главной
    PERSONAL_ACCOUNT = (By.XPATH, '//*[text()="Личный Кабинет"]') #кнопка "Личный кабинет"
    BUN_TUB_CONSTRUCTOR = (By.XPATH, './/span[text()="Булки"]/..') #название вкладки "Булки"
    BUN_MENU_TITLE = (By.XPATH, './/*[(contains(@class,"text_type_main-medium")) and text()="Булки"]') #название раздела "Булки" в меню
    SAUCE_TUB_CONSTRUCTOR = (By.XPATH, './/span[text()="Соусы"]/..') #название вкладки "Соусы"
    SAUCE_MENU_TITLE = (By.XPATH, './/*[(contains(@class,"text_type_main-medium")) and text()="Соусы"]') #название раздела "Соусы" в меню
    FILLING_TUB_CONSTRUCTOR = (By.XPATH, './/span[text()="Начинки"]/..') #название вкладки "Начинки"
    FILLING_MENU_TITLE = (By.XPATH, './/*[(contains(@class,"text_type_main-medium")) and text()="Начинки"]') #название раздела "Начинки" в меню

    #локаторы на главной странице (после авторизации)
    ORDER_BUTTON_MAIN_PAGE = (By.XPATH, './/button[text()="Оформить заказ"]')  #кнопка "Оформить заказ"

    #локаторы на странице авторизации (входа в личный кабинет)
    EMAIL_INPUT_FORM_LOGIN = (By.XPATH, './/label[text() = "Email"]/following-sibling::input') #поле ввода "Email"
    PASSWORD_INPUT_FORM_LOGIN = (By.XPATH, './/label[text() = "Пароль"]/following-sibling::input') #поле ввода "Пароль"
    LOGIN_BUTTON_LOGIN_PAGE = (By.XPATH, './/button[text()="Войти"]')  #кнопка "Войти"
    LINK_REGISTRATION = (By.XPATH, './/*[@href="/register"]')  #ссылка "Зарегистрироваться"
    LINK_PASSWORD_RECOVERY = (By.XPATH, './/*[@href="/forgot-password"]')  #ссылка "Восстановить пароль"

    #локаторы в Личном кабинете
    LOGOUT_BUTTON = (By.XPATH, './/button[text()="Выход"]') #кнопка "Выход"
    CONSTRUCTOR_BUTTON = (By.XPATH, './/*[text()="Конструктор"]') #кнопка "Конструктор"
    LOGO = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2') #логотип Stellar Burgers

    #локаторы на странице регистрации
    LOGIN_BUTTON_PERSONAL = (By.XPATH, './/*[(contains(@class,"button_button_size_medium")) and text()="Войти"]') #кнопка "Войти"
    NAME_INPUT_FORM_REGISTRATION = (By.XPATH, './/label[text()="Имя"]/following-sibling::input') #поле ввода "Имя"
    EMAIL_INPUT_FORM_REGISTRATION = (By.XPATH, './/label[text() = "Email"]/following-sibling::input') #поле ввода "Email"
    PASSWORD_INPUT_FORM_REGISTRATION = (By.XPATH, './/label[text()="Пароль"]/following-sibling::input') #поле ввода "Пароль"
    BUTTON_REGISTRATION = (By.XPATH, './/button[text()="Зарегистрироваться"]') #кнопка "Зарегистрироваться"
    PASSWORD_ERROR_MESSAGE = (By.XPATH, './/*[text()="Некорректный пароль"]') #сообщение об ошибке при некорретном пароле
    BUTTON_LOGIN_FORM_REGISTRATION = (By.XPATH, './/*[@href="/login"]') #ссылка "Войти"

    #локаторы в форме восстановления пароля
    BUTTON_LOGIN_FORGOT_PASSWORD_FORM = (By.XPATH, './/*[@href="/login"]') #ссылка "Войти"
