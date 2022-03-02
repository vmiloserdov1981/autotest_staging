from selenium.webdriver.common.by import By


class BasePageLocators():
    USER_ICON_CS = (By.CSS_SELECTOR, "#main_content > div > header > div.Header-module_User_2Rj6kcRxQQedhnZXdlrqWG > div > div")
    GO_TO_CAMPAIGN_PAGE_BTN = (By.CSS_SELECTOR, "#main_content > div > header > div.Header-module_Navbar_oC10rX6SGmKcubtfg-6Fu > a:nth-child(2)")
    GO_TO_ACCOUNTS_PAGE_BTN = (By.CSS_SELECTOR, "#main_content > div > header > div.Header-module_Navbar_oC10rX6SGmKcubtfg-6Fu > a:nth-child(3)")
    GO_TO_STATISTICS_PAGE_BTN = (By.CSS_SELECTOR, "#main_content > div > header > div.Header-module_Navbar_oC10rX6SGmKcubtfg-6Fu > a:nth-child(4)")
    CHOICE_ADVERTISER_RECKITT_BENCKISER_BTN = (By.CSS_SELECTOR, "#main_content > div > header > div.Header-module_InfoWrapper_kbZsX3uIymxZbCP1rPss6 > div > div > div > div.css-1wy0on6.react-select__indicators > div > i")
    CHOICE_ADVERTISER_RECKITT_BENCKISER_BTN2 = (By.CSS_SELECTOR, "#react-select-2-input")

    CHOICE_ADVERTISER_UNILEVER_BTN = (By.CSS_SELECTOR, "#main_content > div > header > div.Header-module_AdvertiserContainer_1lE9tNxbfGG-eKaFRDnRJY > div > div > div.css-z8ex4e.react-select__value-container.react-select__value-container--has-value")
    CHOICE_ADVERTISER_UNILEVER_BTN2 = (By.CSS_SELECTOR, "#react-select-2-input")

    GO_TO_ADMINISTRATION_PAGE_BTN = (By.CSS_SELECTOR, "#main_content > div > header > div.Header-module_User_2Rj6kcRxQQedhnZXdlrqWG > div > img")
    GO_TO_ADMINISTRATION_PAGE_BTN2 = (By.CSS_SELECTOR, "#main_content > div > header > div.Header-module_User_2Rj6kcRxQQedhnZXdlrqWG > ul > li:nth-child(1) > a")
    GO_TO_ADVERTISER_LINKS_POWER_BI = (By.CSS_SELECTOR, "#main_content > div > main > div > aside > ul > li:nth-child(5) > a")
    SCROLL_DOWN_TO_ADD_BUTTON = (By.CSS_SELECTOR, "#react-tabs-5 > div > div:nth-child(3) > div > button")
    BASE_PAGE_CLICK = (By.CSS_SELECTOR, "#main_content > div > main > div > section > div > div.PowerbiAdvertiserSettings-module_Layout_kBaiBZM1T2VMqK96VopLU > div > div.PowerbiAdvertiserSettings-module_Form_146jI4j5_rDd_MQ_Pl4Std > h2")
    CHOICE_CUSTOM_NAME_BTN = (By.CSS_SELECTOR, "#react-tabs-1 > div > div:nth-child(3) > div > table > tbody > tr:nth-child(4) > td:nth-child(1) > input")
    CHOICE_CUSTOM_URL_BTN = (By.CSS_SELECTOR, "#react-tabs-1 > div > div:nth-child(3) > div > table > tbody > tr:nth-child(4) > td:nth-child(2) > input")
    CHOICE_CUSTOM_BTN_CHECKBOX = (By.CSS_SELECTOR, "#react-tabs-1 > div > div:nth-child(3) > div > table > tbody > tr:nth-child(4) > td:nth-child(3) > label > label > div")
    SAVE_CUSTOM_BTN = (By.CSS_SELECTOR, "#main_content > div > main > div > section > div > div.PowerbiAdvertiserSettings-module_Layout_kBaiBZM1T2VMqK96VopLU > div > div.PowerbiAdvertiserSettings-module_Form_146jI4j5_rDd_MQ_Pl4Std > div.PowerbiAdvertiserSettings-module_Save_2TrDTYPt9sRRUF4rt8eifc > button")
    CHECK_CREATE_CUSTOM_BTN = (By.CSS_SELECTOR, "#main_content > div > main > div > div.Brands-module_Summary_4-jUz8QRn3mD26pfAwQpk > div.Brands-module_SummaryCustomButtonsContainer_2FjbOu4PFXHe4pH8_k4zZX > button:nth-child(3) > div")
    DELETE_CUSTOM_BTN = (By.CSS_SELECTOR, "#react-tabs-1 > div > div:nth-child(3) > div > table > tbody > tr:nth-child(4) > td:nth-child(4) > button")
    SAVE_DELETE_CUSTOM_BTN = (By.CSS_SELECTOR, "#main_content > div > main > div > section > div > div.PowerbiAdvertiserSettings-module_Layout_kBaiBZM1T2VMqK96VopLU > div > div.PowerbiAdvertiserSettings-module_Form_146jI4j5_rDd_MQ_Pl4Std > div.PowerbiAdvertiserSettings-module_Save_2TrDTYPt9sRRUF4rt8eifc > button")


class CampaignPageLocators():
    ADD_NEW_CAMPAIGN_BTN = (By.CSS_SELECTOR, "#main_content > div > main > div > div.Campaigns-module_Header_1ln_h2Yh14IhTRID2x0apT > a > button")
    FILL_IN_THE_CAMPAIGN_AUTOMATICALLY_BTN = (By.CSS_SELECTOR, "#main_content > div > main > div > section > form > div:nth-child(3) > button")
    SELECT_FILE_BTN = (By.CSS_SELECTOR, "body > div.swal-overlay.swal-overlay--show-modal > div > div.swal-content > div > div.FileUploader-module_root_2bpDXtrBY2UEV341pfIZq7 > input")
    SHEET_CONTAINING_CAMPAIGN_CARD_BTN0 = (By.CSS_SELECTOR, "body > div.swal-overlay.swal-overlay--show-modal > div > div.swal-content > div > div.css-2b097c-container > div")
    SHEET_CONTAINING_CAMPAIGN_CARD_BTN = (By.CSS_SELECTOR, "#react-select-10-input")
    AUTO_CARD_CREATE_SAVE_BUTTON = (By.CSS_SELECTOR, "body > div.swal-overlay.swal-overlay--show-modal > div > div.swal-footer > div:nth-child(2) > button")
    AUTO_CARD_CREATE_BUTTON_SAVE_TOTAL = (By.CSS_SELECTOR, "#main_content > div > main > div > section > form > div.CampaignEdit-module_ButtonGroup_1zTcwE208JwwEmiejQdwoH > div:nth-child(2) > button:nth-child(2)")
    FILL_STATUS_BTN = (By.CSS_SELECTOR, "#main_content > div > main > div > section > form > div.CampaignEdit-module_Form_3y8hjc4Um-LNjkm5v7fb25 > fieldset:nth-child(1) > div:nth-child(3) > div:nth-child(2) > label > div > div > div > div.css-tntsk8.react-select__value-container > div.css-8n9vvk-placeholder.react-select__placeholder")
    FILL_STATUS_BTN_INPUT = (By.XPATH, '//*[@id="react-select-41-input"]')
    FILL_STATUS_BTN_INPUT2 = (By.CSS_SELECTOR, "#react-select-8-input")
    CAMPAIGN_AUTO_CREATE_NAME = (By.CSS_SELECTOR, "#main_content > div > main > div > div.CampaignView-module_Campaign_1PJQRwJRLV9-1pI12ABXJX > section > header > div > div > h1")
    DELETE_TEST_CAMPAIGN_BTN = (By.CSS_SELECTOR, "#main_content > div > main > div > section > header > i")
    DELETE_TEST_CAMPAIGN_BTN2 = (By.CSS_SELECTOR, "body > div.swal-overlay.swal-overlay--show-modal > div > div.swal-footer > div:nth-child(2) > button")
    EDIT_TEST_CAMPAIGN_BTN = (By.CSS_SELECTOR, "#main_content > div > main > div > div.CampaignView-module_Campaign_1PJQRwJRLV9-1pI12ABXJX > section > header > a > i")
    CLICK_PAGE_DOWNLOAD_STATISTICS = (By.CSS_SELECTOR, "#main_content > div > header > div.Header-module_Navbar_oC10rX6SGmKcubtfg-6Fu > a:nth-child(4)")
    SELECT_FILE_STATISTICS_BTN = (By.CSS_SELECTOR, "#main_content > div > main > div > section.UploadStatistics-module_Uploader_1wfmbWplR8QouBwuMME9gk > div > input")
    CHECK_STATISTICS_LOADING_STATUS = (By.CSS_SELECTOR, "#main_content > div > main > div > section.UploadStatistics-module_Files_2YC68B0iGQpNXqcC__WwJ7 > div.UploadStatistics-module_FilesColumn_1Z3phKPePMV6EezT7LaHq- > table > tbody > tr:nth-child(1) > td:nth-child(5) > div > i")
    CAMPAIGN_PAGE_CLICK = (By.CSS_SELECTOR, "#main_content > div > header > div.Header-module_Navbar_oC10rX6SGmKcubtfg-6Fu > a:nth-child(2)")


class ProgrammaticPageLocators():
    CLICK_LOG_BTN = (By.CSS_SELECTOR, "#pr_id_4_content > div > div > div.ControlPanel-module_actions_2S_gDbRYR3TYbGNPaNa0Pk > div > button:nth-child(3) > span.p-button-label.p-c")
    STATISTIC_BTN = (By.CSS_SELECTOR, "#pr_id_8_header_0 > span")

#class MainPageLocators():
#    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    USER_EMAIL = (By.CSS_SELECTOR, "#mail")
    USER_PASS = (By.CSS_SELECTOR, "#password")
    LOGIN_BTN = (By.CSS_SELECTOR, ".Auth-module_FormButton_33oas1VJ77STNXmaFXNJMN")

class AdministrationLocators():
    ADVERTISER_BTN = (By.CSS_SELECTOR, "#main_content > div > main > div > aside > ul > li:nth-child(1) > a")
    SELECT_LOGO_FILE_BTN = (By.CSS_SELECTOR, "#main_content > div > main > div > section > div > div:nth-child(1) > div > div > div.LogoPreview-module_Content_35qcUQhdXsnqCPfP3CpvYl > div > button.Button-module_Button_2YI99q3RebaqtAPp3sbzy.Button-module_ButtonLight_mYLvDV-8FNPH0QQ63FVHE > input")
    SAVE_LOGO_BTN = (By.CSS_SELECTOR, "#main_content > div > main > div > section > div > div:nth-child(1) > header > div > button:nth-child(2)")
    CHOICE_ADVERTISER_RECKITT_BENCKISER_BTN = (By.CSS_SELECTOR, "#main_content > div > header > div.Header-module_InfoWrapper_kbZsX3uIymxZbCP1rPss6 > div > div > div > div.css-1wy0on6.react-select__indicators > div > i")
    CHOICE_ADVERTISER_RECKITT_BENCKISER_BTN2 = (By.CSS_SELECTOR, "#react-select-2-input")
    LOGO_JPG  = (By.CSS_SELECTOR, "#main_content > div > main > div > section > div > div:nth-child(1) > div > div > div.LogoPreview-module_Preview_2O19TY6f4lnk-sLouewFYR > div > img")
    DEL_ADVERTISER_LOGO = (By.CSS_SELECTOR, "#main_content > div > main > div > section > div > div:nth-child(1) > div > div > div.LogoPreview-module_Content_35qcUQhdXsnqCPfP3CpvYl > div > button.Button-module_Button_2YI99q3RebaqtAPp3sbzy.Button-module_ButtonTransparentDanger_-wlxR7sCENptatLtp5Knx")



class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".add-to-basket button")
    ADDED_PRODUCT_TEXT = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    BASKET_PRICE_TEXT = (By.CSS_SELECTOR, ".alertinner p strong")
    PRODUCT_NAME_TEXT = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE_TEXT = (By.CSS_SELECTOR, ".product_main .price_color")
    INFO_MESSAGE = (By.XPATH, "//div[contains(@class, 'alert-info')] //p[not(.//a)]")


class BasketPageLocators():
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS_HEADER = (By.CSS_SELECTOR, ".basket-items")
