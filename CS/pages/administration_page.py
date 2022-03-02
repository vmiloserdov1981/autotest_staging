from .base_page import BasePage
import time
from .locators import BasePageLocators
from .locators import CampaignPageLocators
from selenium.webdriver.common.keys import Keys
from .locators import LoginPageLocators
from .locators import CampaignPageLocators
from .locators import BasePageLocators
from .locators import AdministrationLocators
from selenium.webdriver.common.keys import Keys

class AdministrationPage(BasePage):
    def __init__(self, browser):
        self.page_url = "administration"
        super().__init__(browser, BasePage.site_url + "/" + self.page_url)

    def choice_advertiser_autotest_only(self, autotest_only):
        self.browser.find_element(*AdministrationLocators.CHOICE_ADVERTISER_RECKITT_BENCKISER_BTN).click()
        time.sleep(1)
        self.browser.find_element(*AdministrationLocators.CHOICE_ADVERTISER_RECKITT_BENCKISER_BTN2).send_keys(autotest_only)
        time.sleep(1)
        self.browser.find_element(*AdministrationLocators.CHOICE_ADVERTISER_RECKITT_BENCKISER_BTN2).send_keys(Keys.ENTER)
        time.sleep(1)

    def click_on_advertiser_btn(self):
        self.browser.find_element(*AdministrationLocators.ADVERTISER_BTN).click()

    def click_on_upload_advertiser_logo(self, string_filepath_logo):
        self.browser.find_element(*AdministrationLocators.SELECT_LOGO_FILE_BTN).send_keys(string_filepath_logo)
        time.sleep(0.3)
        self.browser.find_element(*AdministrationLocators.SAVE_LOGO_BTN).click()

    def should_be_logo_jpg(self):
        assert self.is_element_present(*AdministrationLocators.LOGO_JPG), \
            "Логотип рекламодателя не загрузился !!!"

    def delete_logo_jpg(self):
        self.browser.find_element(*AdministrationLocators.DEL_ADVERTISER_LOGO).click()
        time.sleep(0.3)
        self.browser.find_element(*AdministrationLocators.SAVE_LOGO_BTN).click()



#    def uploading_advertiser_logo_file(self, string_filepath_logo):
#       self.browser.find_element(*AdministrationLocators.FILL_IN_THE_CAMPAIGN_AUTOMATICALLY_BTN).click()
#       self.browser.find_element(*AdministrationLocators.SELECT_FILE_BTN).send_keys(string_filepath_logo)
#       time.sleep(0.5)

