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
