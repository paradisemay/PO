import time

import pytest

from .pages.locators import ProductPageLocators
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser,
                       ProductPageLocators.LINK)
    page.open()
    page.can_add_to_basket()


@pytest.mark.xfail()
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.LINK)
    page.open()
    page.click_to_basket_button()
    page.should_not_be_successful_message_1()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, ProductPageLocators.LINK)
    page.open()
    page.should_not_be_successful_message_2()


@pytest.mark.xfail()
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.LINK)
    page.open()
    page.click_to_basket_button()
    page.should_not_be_successful_message_3()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/'
    page = ProductPage(browser, link)
    page.open()
    page.click_to_main_basket_button()
    page.should_be_empty_basket()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        self.browser = browser
        page = LoginPage(self.browser, 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/')
        page.open()
        page.register_new_user(str(time.time()) + '@fakemail.org', 'wqdafdsfw34fw4f2r1f2q1JURSuRJXsjX')
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(self.browser,
                           'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/')
        page.open()
        page.can_add_to_basket()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(self.browser,
                           'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/')
        page.open()
        page.should_not_be_successful_message_2()
