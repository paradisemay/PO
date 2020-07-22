import math

from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def can_add_to_basket(self):
        self.should_be_basket_button()
        self.should_be_correct_name()
        self.should_be_correct_price()
        self.click_to_basket_button()
        self.solve_quiz_and_get_code()
        self.should_be_successful_message()
        print(f'Name: {self.name}; Price: {self.price}')

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), 'Basket button not present'

    def click_to_basket_button(self):
        self.browser.find_element(*ProductPageLocators.BASKET_BUTTON).click()

    def should_be_correct_name(self):
        self.name = self.browser.find_element(*ProductPageLocators.NAME_SELECTOR).text

    def should_be_correct_price(self):
        self.price = self.browser.find_element(*ProductPageLocators.PRICE_SELECTOR).text.split(' ')[0]

    def should_be_successful_message(self):
        # first name, second price
        name = self.browser.find_element(*ProductPageLocators.AFTER_NAME_SELECTOR).text
        assert name in self.name, f'After "{name}" not equal before "{self.name}"'
        price = self.browser.find_element(*ProductPageLocators.AFTER_PRICE_SELECTOR).text.split(' ')[0]
        assert price in self.price, f'After "{price}" not equal before "{self.price}"'
