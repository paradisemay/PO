from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LINK_LIST = [
        'http://selenium1py.pythonanywhere.com/',
        'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer'
    ]
    LINK = LINK_LIST[0]


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD1 = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REG_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    LINKS = [
        'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear',
        'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019',
        'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
    ]
    LINK = LINKS[2]
    NAME_SELECTOR = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > h1')
    PRICE_SELECTOR = (By.CSS_SELECTOR, 'div.col-sm-6.product_main > p.price_color')
    AFTER_NAME_SELECTOR = (By.CSS_SELECTOR, 'div.alertinner > strong')
    AFTER_PRICE_SELECTOR = (By.CSS_SELECTOR, 'div.alertinner > p > strong')
    SUCCESSFUL_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    MAIN_BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini a.btn.btn-default')
    BASKET_TEXT = (By.CSS_SELECTOR, '#content_inner > p')
    TRUE_BASKET_TEXT = 'Your basket is empty'
    ELEMENTS_IN_BASKET = (By.CSS_SELECTOR, '.basket-items')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    MAIN_BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini a.btn.btn-default')
    BASKET_TEXT = (By.CSS_SELECTOR, '#content_inner > p')
    TRUE_BASKET_TEXT = 'Your basket is empty'
    ELEMENTS_IN_BASKET = (By.CSS_SELECTOR, '.basket-items')
