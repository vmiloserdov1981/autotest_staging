from .base_page import BasePage
import time
from .locators import BasePageLocators
from .locators import CampaignPageLocators
from selenium.webdriver.common.keys import Keys
from .locators import LoginPageLocators
from .locators import CampaignPageLocators
from .locators import BasePageLocators
from .locators import ProgrammaticPageLocators

class ProgrammaticPage(BasePage):
    def __init__(self, browser):
        self.page_url = "programmatic"
        super().__init__(browser, BasePage.site_url + "/" + self.page_url)


    def login_test_user2(self, name, password):
        self.browser.find_element(*LoginPageLocators.USER_EMAIL).send_keys(name)
        self.browser.find_element(*LoginPageLocators.USER_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BTN).click()

    def click_log_btn(self):
        self.browser.find_element(*ProgrammaticPageLocators.CLICK_LOG_BTN).click()
