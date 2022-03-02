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
        time.sleep(2)

        # Проверка
        page.should_be_logo_jpg()
        time.sleep(0.5)
        page.delete_logo_jpg()
        time.sleep(4)



