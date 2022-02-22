import time
import pytest
from .pages.login_page import LoginPage
from .pages.campaign_page import CampaignPage
from .pages.custom_campaign_page import CustomCampaignPage

class TestAuthorizationPage:


    def test_authorization_user(self, browser):
        # Данные
        name = "testing-user"
        password = "testing-user"
        page = LoginPage(browser)

        # Подготовка
        page.open()

        # Действия
        page.login_test_user(name, password)

        # Проверка
        page.should_be_authorized_user()

    def test_authorization_admin(self, browser):
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

    def test_authorization_client(self, browser):
        # Данные
        name = "Testing-client"
        password = "Testing-client"
        page = LoginPage(browser)

        # Подготовка
        page.open()

        # Действия
        page.login_test_user(name, password)

        # Проверка
        page.should_be_authorized_user()

    def test_checking_client_role(self, browser):
        # Данные
        name = "Testing-client"
        password = "Testing-client"
        page = LoginPage(browser)

        # Подготовка
        page.open()

        # Действия
        page.login_test_user(name, password)
        time.sleep(1)
        page.go_to_сampaigns_page()

        # Проверка
        page.checking_client_cannot_create_campaign()

    def test_checking_user_role(self, browser):
        # Данные
        name = "testing-user"
        password = "testing-user"
        page = CustomCampaignPage(browser)

        # Подготовка
        page.open()

        # Действия
        page.login_test_user1(name, password)
        time.sleep(1)
        page.click_on_edit_btn()
        time.sleep(1)

        # Проверка
        page.checking_user_cannot_delete_campaign()