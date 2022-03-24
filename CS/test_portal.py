import time
import pytest
from .pages.login_page import LoginPage
from .pages.campaign_page import CampaignPage
from .pages.custom_campaign_page import CustomCampaignPage
from .pages.administration_page import AdministrationPage

class TestPortal:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # Данные
        name = "testing-admin"
        password = "testing-admin"
        page = LoginPage(browser)

        # Подготовка
        page.open()

        # Действия
        page.login_test_user(name, password)

        # Проверка
        page.should_be_authorized_user()


    def test_change_advertiser_logo(self, browser):
        # Данные
        page = AdministrationPage(browser)
        autotest_only = "Autotest ONLY"
        string_filepath_logo = "C:\Autotest\Brands_page\maxresdefault.jpg"

        # Подготовка
        page.open()

        # Действия
        page.choice_advertiser_autotest_only(autotest_only)
        time.sleep(0.5)
        page.click_on_advertiser_btn()
        time.sleep(0.5)
        page.click_on_upload_advertiser_logo(string_filepath_logo)
        time.sleep(1)

        # Проверка
        page.should_be_logo_advertiser_jpg()
        time.sleep(0.5)
        page.delete_logo_advertiser_jpg()
        time.sleep(4)

    def test_change_brand_logo(self, browser):
        # Данные
        page = AdministrationPage(browser)
        autotest_only = "Autotest ONLY"
        string_filepath_logo = "C:\Autotest\Brands_page\Selenium.jpg"

        # Подготовка
        page.open()

        # Действия
        page.choice_advertiser_autotest_only(autotest_only)
        time.sleep(0.5)
        page.click_on_brand_btn()
        time.sleep(0.5)
        page.click_on_upload_brand_logo(string_filepath_logo)
        time.sleep(1)
        page.goto_brand_page()

        # Проверка
        page.should_be_logo_brand_jpg()
        time.sleep(0.5)
        page.open()
        time.sleep(0.5)
        page.click_on_brand_btn()
        page.delete_logo_brand_jpg()
        time.sleep(4)

    def test_creating_dashboard_buttons_on_brand_page(self, browser):
        # Данные
        page = AdministrationPage(browser)
        autotest_only = "Autotest ONLY"
        dashboard_btn_url = 'https://sqlzoo.net/'

        # Подготовка
        page.open()
        time.sleep(2)

        page.choice_advertiser_autotest_only(autotest_only)
        time.sleep(1)
        page.go_to_advertiser_links_power_bi()
        time.sleep(1)
        page.create_title_and_link_for_custom_button(dashboard_btn_url)
        time.sleep(1)

'''
        # Проверка
        time.sleep(1)
        page.check_new_custom_btn(custom_btn_name2)
        time.sleep(1)

        #удаление кнопки
        page.go_to_administration_page()
        time.sleep(1)
        page.go_to_advertiser_links_power_bi2()
        time.sleep(1)
        page.delete_custom_btn()
'''