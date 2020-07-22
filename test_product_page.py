import time

import pytest

from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage


@pytest.mark.skip()
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_go_to_login_page(browser, link):
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.can_add_to_basket()  # можно ли добавить в корзину


@pytest.mark.skip()
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.LINK)
    page.open()
    page.click_to_basket_button()
    before = time.time()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESSFUL_MESSAGE, timeout=4)
    after = time.time()
    print(f'#1 {after - before} s')


@pytest.mark.skip()
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, ProductPageLocators.LINK)
    page.open()
    # page.click_to_basket_button()
    before = time.time()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESSFUL_MESSAGE, timeout=4)
    after = time.time()
    print(f'#2 {after - before} s')


@pytest.mark.skip()
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocators.LINK)
    page.open()
    page.click_to_basket_button()
    before = time.time()
    assert page.is_disappeared(*ProductPageLocators.SUCCESSFUL_MESSAGE, timeout=4)
    after = time.time()
    print(f'#3 {after - before} s')
