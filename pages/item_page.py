from .base_page import BasePage
from .locators import ItemPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ItemPage(BasePage):
    def add_item_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ItemPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_btn.click()

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

    def should_be_correct_name(self):
        item_name = self.browser.find_element(*ItemPageLocators.ITEM_NAME).text
        message_item_name = self.browser.find_element(*ItemPageLocators.MESSAGE_ITEM_NAME).text
        assert item_name == message_item_name, 'wrong item name'

    def should_be_correct_price(self):
        item_price = self.browser.find_element(*ItemPageLocators.ITEM_PRICE).text
        message_item_price = self.browser.find_element(*ItemPageLocators.MESSAGE_ITEM_PRICE).text
        assert item_price == message_item_price, 'wrong item price'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ItemPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ItemPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should be disappeared"
