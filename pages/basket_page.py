from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def click_to_main_basket_button(self):
        self.browser.find_element(*BasePageLocators.MAIN_BASKET_BUTTON).click()

    def should_be_empty_basket(self):
        text = self.browser.find_element(*BasketPageLocators.BASKET_TEXT).text
        assert BasketPageLocators.TRUE_BASKET_TEXT in text, f'Basket is not empty: {text}'
        assert self.is_not_element_present(*BasketPageLocators.ELEMENTS_IN_BASKET)
