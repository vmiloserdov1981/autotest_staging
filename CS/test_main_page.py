from .pages.main_page import MainPage
import time
import pytest
from .pages.login_page import LoginPage
from selenium import webdriver
#from pages.basket_page import BasketPage
#from pages.product_page import ProductPage

class TestUserLogin():
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


    def test_user_stays_on_campaign_page_after_reload(self, browser):
        # Данные
        page = MainPage(browser)

        # Подготовка
        page.open()
        time.sleep(4)
        page.go_to_campaign_page()
        time.sleep(1)

        # Действие
        page.reload()
        time.sleep(1)

        # Проверка
        page.check_url_campaign_page()
        time.sleep(1)

    def test_user_stays_on_accounts_page_after_reload(self, browser):
        # Данные
        page = MainPage(browser)

        # Подготовка
        page.open()
        time.sleep(4)
        page.go_to_accounts_page()
        time.sleep(1)

        # Действие
        page.reload()
        time.sleep(1)

        # Проверка
        page.check_url_accounts_page()
        time.sleep(1)

    def test_user_stays_on_statistics_page_after_reload(self, browser):
        # Данные
        page = MainPage(browser)

        # Подготовка
        page.open()
        time.sleep(4)
        page.go_to_statistics_page()
        time.sleep(1)

        # Действие
        page.reload()
        time.sleep(1)

        # Проверка
        page.check_url_statistics_page()
        time.sleep(1)
        

    def test_creating_custom_advertiser_buttons_on_brand_page(self, browser):
        # Данные
        page = MainPage(browser)
        Unilever = "Unilever"
        custom_btn_name = 'AUTOtest'
        custom_btn_name2 = 'AUTOtest'
        custom_btn_url = 'https://yandex.ru/'

        # Подготовка
        page.open()
        time.sleep(4)
        page.choice_advertiser_unilever2(Unilever)
        time.sleep(1)
        page.go_to_administration_page()
        time.sleep(1)
        page.go_to_advertiser_links_power_bi()
        time.sleep(1)
        page.create_title_and_link_for_custom_button(custom_btn_name, custom_btn_url)
        time.sleep(1)
        page.open()
        time.sleep(3)

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





