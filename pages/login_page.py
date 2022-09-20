from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        cur_url = self.browser.current_url
        assert '/accounts/login/' in cur_url, 'URL address is wrong'
        print(1)

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        print(2)

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        print(3)

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        repeat_field = self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_FIELD)
        repeat_field.send_keys(password)
        btn = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        btn.click()
