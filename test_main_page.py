from .pages.locators import MainPageLocators
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


# @pytest.mark.skip()
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser,
                    MainPageLocators.LINK)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина


# @pytest.mark.skip()
def test_guest_should_see_login_link(browser):
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()
    page.should_be_login_link()


def test_guest_should_see_login_page(browser):
    page = MainPage(browser, MainPageLocators.LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
