from .base_page import BasePage
import time
from .locators import BasePageLocators
from .locators import CampaignPageLocators
from selenium.webdriver.common.keys import Keys
from .locators import LoginPageLocators
from .locators import CampaignPageLocators
from .locators import BasePageLocators

class CustomCampaignPage(BasePage):
    def __init__(self, browser):
        self.page_url = "campaigns"
        self.custom_url = "101544"
        super().__init__(browser, BasePage.site_url + "/" + self.page_url + "/" + self.custom_url)

    def login_test_user1(self, name, password):
        self.browser.find_element(*LoginPageLocators.USER_EMAIL).send_keys(name)
        self.browser.find_element(*LoginPageLocators.USER_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BTN).click()

    def click_on_edit_btn(self):
        self.browser.find_element(*CampaignPageLocators.EDIT_TEST_CAMPAIGN_BTN).click()
