from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    GO_TO_BASKET_BTN = (By.CSS_SELECTOR, '.btn-group .btn:nth-child(1)')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password1')
    REPEAT_PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password2')
    SUBMIT_BUTTON = (By.NAME, 'registration_submit')


class ItemPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    ITEM_NAME = (By.CSS_SELECTOR, '.product_main h1')
    ITEM_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    MESSAGE_ITEM_NAME = (By.CSS_SELECTOR, 'div#messages .alert:nth-child(1) .alertinner strong')
    MESSAGE_ITEM_PRICE = (By.CSS_SELECTOR, '.alertinner>p>strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(1)")


class BasketPageLocators:
    EMPTY_BASKET_MESS = (By.CSS_SELECTOR, '#content_inner p')
    BASKET_FORMSET = (By.CSS_SELECTOR, '.basket_summary')
    HEADER = (By.CSS_SELECTOR, '.page-header')
