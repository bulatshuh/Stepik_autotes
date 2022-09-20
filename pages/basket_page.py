from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_message_about_empty_basket(self):
        empty_mess = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESS).text
        assert 'Your basket is empty' in empty_mess, 'WRONG MESSAGE ABOUT EMPTY BASKET'

    def should_be_no_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET), \
            'Items presented,but should not be'
