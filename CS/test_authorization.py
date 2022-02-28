import time
import pytest
from .pages.login_page import LoginPage
from .pages.campaign_page import CampaignPage
from .pages.custom_campaign_page import CustomCampaignPage
from .pages.Programmatic_page import ProgrammaticPage

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

    def test_checking_admin_role(self, browser):
        # Данные
        name = "testing-admin"
        password = "testing-admin"
        page = CustomCampaignPage(browser)

        # Подготовка
        page.open()

        # Действия
        page.login_test_user1(name, password)
        time.sleep(2)
        page.click_on_edit_btn()
        time.sleep(1)

        # Проверка
        page.checking_admin_can_delete_campaign()

    def test_checking_ProgrammaticManager_role(self, browser):
        # Данные
        name = "testing-user"
        password = "testing-user"
        page = ProgrammaticPage(browser)

        # Подготовка
        page.open()

        # Действия
        page.login_test_user2(name, password)
        time.sleep(2)
        page.click_log_btn()
        time.sleep(2)

        # Проверка
        page.checking_available_statistics_buttons()




    @pytest.mark.xfail(reason="invalid test case")
    def test_authorization_incorrect_password(self, browser):
        # Данные
        name = "testing-user"
        password = "testinuse5635r"
        page = LoginPage(browser)

        # Подготовка
        page.open()

        # Действия
        page.login_test_user(name, password)

        # Проверка
        page.should_be_authorized_user()

    @pytest.mark.xfail(reason="invalid test case")
    def test_authorization_incorrect_login(self, browser):
        # Данные
        name = "123"
        password = "testing-user"
        page = LoginPage(browser)

        # Подготовка
        page.open()

        # Действия
        page.login_test_user(name, password)

        # Проверка
        page.should_be_authorized_user()

    @pytest.mark.xfail(reason="invalid test case")
    def test_authorization_without_password_and_login(self, browser):
        # Данные
        name = ""
        password = ""
        page = LoginPage(browser)

        # Подготовка
        page.open()

        # Действия
        page.login_test_user(name, password)

        # Проверка
        page.should_be_authorized_user()