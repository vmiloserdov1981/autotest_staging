import time
import pytest
from .pages.login_page import LoginPage
from .pages.campaign_page import CampaignPage


class TestProductPage:

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


    def test_campaign_cards_auto_complete(self, browser):
        # Данные
        page = CampaignPage(browser)
        reckitt_benckiser = "Reckitt Benckiser"
        string_filepath = "C:\Autotest\campaign_cards_auto_complete\Test_reckitt benckiser_4.xlsx"
        campaing_name = "Auto1301_10"
#        campaing_name = "Ayterwrr"

        # Подготовка
        page.open()
        time.sleep(3)
        page.choice_advertiser_reckitt_benckiser(reckitt_benckiser)
        time.sleep(1)
        page.choice_add_new_campaign()
        time.sleep(1)
        page.fill_in_the_campaign_automatically(string_filepath)
        time.sleep(1)

        # Действие
        page.create_campaign_from_automatically_entered_data()

        # Проверка
        page.get_auto_campaign_name(campaing_name)
        time.sleep(4)

        # Удаление ненужной кампании
        page.delete_test_campaign()
        time.sleep(2)


    def test_loading_statistics_for_campaign(self, browser):
        # Подготовка
        page = CampaignPage(browser)
        Unilever = "Unilever"
        string_filepath_loading_statistics = "C:\Autotest\loading_statistics\Autotest_statistics_loading.xlsx"
        file_uploaded_successfully = "Загружено"
        page.open()
        time.sleep(3)
        page.choice_advertiser_unilever(Unilever)
        time.sleep(1)

        # Действие
        page.go_to_the_page_download_statistics()
        page.download_statistics_file(string_filepath_loading_statistics)
        time.sleep(5)

        # Проверка
        page.reload()
        time.sleep(3)
        page.check_file_loaded_successfully(file_uploaded_successfully)

    '''
    def test_cabinet_mediaplan_for_data_saving(self, browser):
        # Подготовка
        page = CampaignPage(browser)
        Unilever = "Unilever"
        cabinet_test_campaign = 'ONLY_FOR_AUTOTEST'
        value_utm_label_for_ga = 'utm_term=klychevaya_fraza'
        value_for_cabinet_weborama = '154645646'
        value_search_cabinet_ga = 'googleanalytics'
        value_search_cabinet_weborama = 'weborama'
        campaign_id_cabinet = '11223344'
        account_id_cabinet = '45671'
        ga_id_param = '234977575'

        time.sleep(3)
        page.choice_advertiser_unilever(Unilever)
        page.search_campaign_to_check_cabinet()
        page.search_campaign_to_check_cabinet_and_enter()
        page.enter_the_cabinet_mediaplan()

        # Действие
        page.seaech_cabinet_ga()
        page.entering_values_for_cabinet_ga_and_save()
        page.seaech_cabinet_weborama()
        page.entering_values_for_cabinet_weborama_and_save()

        # Проверка

'''







