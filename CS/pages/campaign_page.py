from .base_page import BasePage
import time
from .locators import BasePageLocators
from .locators import CampaignPageLocators
from selenium.webdriver.common.keys import Keys

class CampaignPage(BasePage):
    def __init__(self, browser):
        self.page_url = "campaigns"
        super().__init__(browser, BasePage.site_url + "/" + self.page_url)

    def delete_test_campaign(self):
        self.browser.find_element(*CampaignPageLocators.EDIT_TEST_CAMPAIGN_BTN).click()
        time.sleep(1)
        self.browser.find_element(*CampaignPageLocators.DELETE_TEST_CAMPAIGN_BTN).click()
        time.sleep(1)
        self.browser.find_element(*CampaignPageLocators.DELETE_TEST_CAMPAIGN_BTN2).click()


    def get_auto_campaign_name(self, campaing_name):
#        return self.get_element_text(*CampaignPageLocators.CAMPAIGN_AUTO_CREATE_NAME)
        assert campaing_name == self.browser.find_element(*CampaignPageLocators.CAMPAIGN_AUTO_CREATE_NAME).text, "Компания создалась некорректно"

    def check_file_loaded_successfully(self, file_uploaded_successfully):

        assert file_uploaded_successfully == self.browser.find_element(
            *CampaignPageLocators.CHECK_STATISTICS_LOADING_STATUS).get_attribute("title"), "!!! ОШИБКА загрузки файла !!!"

    def choice_advertiser_reckitt_benckiser(self, reckitt_benckiser):
        self.browser.find_element(*BasePageLocators.CHOICE_ADVERTISER_RECKITT_BENCKISER_BTN).click()
        time.sleep(1)
        self.browser.find_element(*BasePageLocators.CHOICE_ADVERTISER_RECKITT_BENCKISER_BTN2).send_keys(reckitt_benckiser)
        time.sleep(1)
        self.browser.find_element(*BasePageLocators.CHOICE_ADVERTISER_RECKITT_BENCKISER_BTN2).send_keys(Keys.ENTER)
        time.sleep(1)

    def choice_advertiser_unilever(self, Unilever):
        self.browser.find_element(*BasePageLocators.CHOICE_ADVERTISER_RECKITT_BENCKISER_BTN).click()
        time.sleep(1)
        self.browser.find_element(*BasePageLocators.CHOICE_ADVERTISER_RECKITT_BENCKISER_BTN2).send_keys(Unilever)
        time.sleep(1)
        self.browser.find_element(*BasePageLocators.CHOICE_ADVERTISER_RECKITT_BENCKISER_BTN2).send_keys(Keys.ENTER)
        time.sleep(1)

    def choice_add_new_campaign(self):
        self.browser.find_element(*CampaignPageLocators.ADD_NEW_CAMPAIGN_BTN).click()
        time.sleep(1)

    def go_to_the_page_download_statistics(self):
        self.browser.find_element(*CampaignPageLocators.CLICK_PAGE_DOWNLOAD_STATISTICS).click()
        time.sleep(1)


    def fill_in_the_campaign_automatically(self, string_filepath):
        self.browser.find_element(*CampaignPageLocators.FILL_IN_THE_CAMPAIGN_AUTOMATICALLY_BTN).click()
        time.sleep(1)
        self.browser.find_element(*CampaignPageLocators.SELECT_FILE_BTN).send_keys(string_filepath)
        time.sleep(1)
        self.browser.find_element(*CampaignPageLocators.SHEET_CONTAINING_CAMPAIGN_CARD_BTN0).click()
        time.sleep(1)
        self.browser.find_element(*CampaignPageLocators.SHEET_CONTAINING_CAMPAIGN_CARD_BTN).send_keys("med")
        time.sleep(1)
        self.browser.find_element(*CampaignPageLocators.SHEET_CONTAINING_CAMPAIGN_CARD_BTN).send_keys(Keys.ENTER)
        time.sleep(1)
        self.browser.find_element(*CampaignPageLocators.AUTO_CARD_CREATE_SAVE_BUTTON).send_keys(Keys.ENTER)
        time.sleep(1)
        self.browser.find_element(*CampaignPageLocators.FILL_STATUS_BTN).click()
        self.browser.find_element(*CampaignPageLocators.FILL_STATUS_BTN_INPUT2).send_keys("Акт")
        time.sleep(1)
        self.browser.find_element(*CampaignPageLocators.FILL_STATUS_BTN_INPUT2).send_keys(Keys.ENTER)

    def download_statistics_file(self, string_filepath_loading_statistics):
        self.browser.find_element(*CampaignPageLocators.SELECT_FILE_STATISTICS_BTN).send_keys(string_filepath_loading_statistics)
        time.sleep(1)


    def create_campaign_from_automatically_entered_data(self):
        self.browser.find_element(*CampaignPageLocators.AUTO_CARD_CREATE_BUTTON_SAVE_TOTAL).click()

