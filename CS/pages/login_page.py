from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import CampaignPageLocators
from .locators import BasePageLocators

class LoginPage(BasePage):
    def __init__(self, browser):
        self.page_url = "auth"
        super().__init__(browser, BasePage.site_url + "/" + self.page_url)

    def login_test_user(self, name, password):
        self.browser.find_element(*LoginPageLocators.USER_EMAIL).send_keys(name)
        self.browser.find_element(*LoginPageLocators.USER_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BTN).click()

    def go_to_сampaigns_page(self):
        self.browser.find_element(*BasePageLocators.GO_TO_CAMPAIGN_PAGE_BTN).click()



    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PROVE_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BTN).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert LoginPageLocators.login_url in self.browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.login_form), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.register_form), "Register form is not presented"