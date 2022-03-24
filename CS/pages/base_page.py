from selenium.webdriver.common.by import By
import math
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators
from selenium.webdriver.common.keys import Keys
from .locators import CampaignPageLocators
from .locators import ProgrammaticPageLocators

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.page_url = ""
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(4)
#        self.browser.implicitly_wait(timeout)  # В конструктор BasePage добавим команду для неявного ожидания со значением по умолчанию в 10

    site_url = "https://clientspace-staging.advcloud.ru"
    campaign_url = "https://clientspace-staging.advcloud.ru/campaigns"
    accounts_page = "https://clientspace-staging.advcloud.ru/accounts"
    statistics_page = "https://clientspace-staging.advcloud.ru/upload-statistics"
    custom_campaign_url = "https://clientspace-staging.advcloud.ru/campaigns"

    def choice_advertiser_reckitt_benckiser(self, reckitt_benckiser):
        link = self.browser.find_element(*BasePageLocators.CHOICE_ADVERTISER_RECKITT_BENCKISER_BTN).click().send_keys(reckitt_benckiser).sendKeys(Keys.ENTER)



    def go_to_campaign_page(self):
#        link = WebDriverWait(self.browser, 5).until(EC.element_to_be_clickable(*BasePageLocators.GO_TO_CAMPAIGN_PAGE_BTN))
        link = self.browser.find_element(*BasePageLocators.GO_TO_CAMPAIGN_PAGE_BTN)
        link.click()

    def go_to_accounts_page(self):
        link = self.browser.find_element(*BasePageLocators.GO_TO_ACCOUNTS_PAGE_BTN)
        link.click()

    def go_to_statistics_page(self):
        link = self.browser.find_element(*BasePageLocators.GO_TO_STATISTICS_PAGE_BTN)
        link.click()

    def go_to_administration_page(self):
        link = self.browser.find_element(*BasePageLocators.GO_TO_ADMINISTRATION_PAGE_BTN)
        link.click()
        time.sleep(2)
        link = self.browser.find_element(*BasePageLocators.GO_TO_ADMINISTRATION_PAGE_BTN2)
        link.click()

    def choice_advertiser_unilever2(self, Unilever):
        link = self.browser.find_element(*BasePageLocators.CHOICE_ADVERTISER_UNILEVER_BTN)
        link.click()
        time.sleep(1)
        link2 = self.browser.find_element(*BasePageLocators.CHOICE_ADVERTISER_UNILEVER_BTN2)
        link2.send_keys(Unilever)
        time.sleep(1)
        link3 = self.browser.find_element(*BasePageLocators.CHOICE_ADVERTISER_UNILEVER_BTN2).send_keys(Keys.ENTER)
        time.sleep(1)


    def go_to_advertiser_links_power_bi(self):
        link = self.browser.find_element(*BasePageLocators.GO_TO_ADVERTISER_LINKS_POWER_BI)
        link.click()
        time.sleep(1)

    def go_to_advertiser_links_power_bi_scroll(self):
        link = self.browser.find_element(*BasePageLocators.GO_TO_ADVERTISER_LINKS_POWER_BI)
        link.click()
        time.sleep(1)
        link = self.browser.find_element(*BasePageLocators.BASE_PAGE_CLICK)
        link.click()
        time.sleep(2)

        link2 = self.browser.find_element_by_css_selector("#react-tabs-1 > div > div:nth-child(3) > div > button")
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", link2)
        link2.click()

    def go_to_advertiser_links_power_bi2(self):
        link = self.browser.find_element(*BasePageLocators.GO_TO_ADVERTISER_LINKS_POWER_BI)
        link.click()
        time.sleep(1)
        link = self.browser.find_element(*BasePageLocators.BASE_PAGE_CLICK)
        link.click()
        time.sleep(1)

        link2 = self.browser.find_element_by_css_selector("#react-tabs-1 > div > div:nth-child(3) > div > button")
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", link2)


    def delete_custom_btn(self):
        link = self.browser.find_element(*BasePageLocators.DELETE_CUSTOM_BTN)
        link.click()
        time.sleep(1)
        link2 = self.browser.find_element(*BasePageLocators.SAVE_DELETE_CUSTOM_BTN)
        link2.click()


    def check_new_custom_btn(self, custom_btn_name2):
        assert custom_btn_name2 == self.browser.find_element(*BasePageLocators.CHECK_CREATE_CUSTOM_BTN).text, "Кастомная кнопка создалась НЕКОРРЕКТНО"

    def create_title_and_link_for_custom_button(self, custom_btn_name, custom_btn_url):
        link = self.browser.find_element(*BasePageLocators.CHOICE_CUSTOM_NAME_BTN)
        link.send_keys(custom_btn_name)
        link2 = self.browser.find_element(*BasePageLocators.CHOICE_CUSTOM_URL_BTN)
        link2.send_keys(custom_btn_url)
        time.sleep(1)
        link3 = self.browser.find_element(*BasePageLocators.CHOICE_CUSTOM_BTN_CHECKBOX)
        link3.click()
        link4 = self.browser.find_element(*BasePageLocators.SAVE_CUSTOM_BTN)
        link4.click()

    def create_title_and_link_for_custom_button(self, custom_btn_name, custom_btn_url):
        link = self.browser.find_element(*BasePageLocators.CHOICE_CUSTOM_NAME_BTN)
        link.send_keys(custom_btn_name)
        link2 = self.browser.find_element(*BasePageLocators.CHOICE_CUSTOM_URL_BTN)
        link2.send_keys(custom_btn_url)
        time.sleep(1)
        link3 = self.browser.find_element(*BasePageLocators.CHOICE_CUSTOM_BTN_CHECKBOX)
        link3.click()
        link4 = self.browser.find_element(*BasePageLocators.SAVE_CUSTOM_BTN)
        link4.click()

    def check_url_campaign_page(self):
        self.should_be_campaign_page()

    def check_url_accounts_page(self):
        self.should_be_accounts_page()

    def check_url_statistics_page(self):
        self.should_be_statistics_page()

    def should_be_campaign_page(self):
        # реализуйте проверку на корректный url адрес
        assert self.campaign_url in self.browser.current_url, "url does not match the campaigns page"

    def should_be_accounts_page(self):
        # реализуйте проверку на корректный url адрес
        assert self.accounts_page in self.browser.current_url, "url does not match the accounts page"

    def should_be_statistics_page(self):
        # реализуйте проверку на корректный url адрес
        assert self.statistics_page in self.browser.current_url, "url does not match the accounts page"


    def open(self):
        self.browser.get(self.url)

    def reload(self):
        self.browser.refresh()








    def get_element_text(self, how, what):
        element = self.browser.find_element(how, what)
        return element

    def check_browser_url(self):
        assert self.browser.current_url.contains(BasePage.site_url)
        assert self.browser.current_url.contains(self.page_url)

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.GO_TO_BASKET_BTN)
        link.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON_CS), "User icon is not presented," \
                                                                     " probably unauthorised user"
    def checking_client_cannot_create_campaign(self):
        assert not self.is_element_present(*CampaignPageLocators.ADD_NEW_CAMPAIGN_BTN), "Ошибка роли КЛИЕНТ - есть кнопка создать кампанию"

    def checking_user_cannot_delete_campaign(self):
        assert not self.is_element_present(*CampaignPageLocators.DELETE_TEST_CAMPAIGN_BTN), "Ошибка роли USER - доступно удаление кампании"

    def checking_admin_can_delete_campaign(self):
        assert self.is_element_present(*CampaignPageLocators.DELETE_TEST_CAMPAIGN_BTN), "Ошибка роли ADMIN - нет кнопки удаления кампании"

    def checking_available_statistics_buttons(self):
        assert self.is_element_present(*ProgrammaticPageLocators.STATISTIC_BTN), "Ошибка роли ProgrammaticManager! Нет кнопки СТАТИСТИКА"




    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def get_element_text(self, how, what):
        element = self.browser.find_element(how, what)
        return element.text

    def get_elements_text(self, how, what):
        elements = self.browser.find_elements(how, what)
        return [element.text for element in elements]


    # реализуем метод is_element_present, в котором будем перехватывать исключение
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    # проверяет, что элемент не появляется на странице в течение заданного времени
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    # проверить, что какой-то элемент исчезает, то следует воспользоваться явным ожиданием
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    # Посчитать результат математического выражения и ввести ответ
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
