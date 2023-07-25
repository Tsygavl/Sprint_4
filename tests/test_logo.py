import allure
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from data import Urls


class TestLogo:

    @allure.title("Проверка перехода на главную страницу Самоката при клике на лого Самоката")
    def test_click_scooter_logo_go_to_samokat_page(self, driver):
        main_page = MainPage(driver)
        driver.get(Urls.samokat_order_page)
        main_page.click_scooter_logo()
        assert main_page.find_element(MainPageLocators.deliver_scooter_for_you), \
            'При клике на лого Самоката переход на главную страницу Самоката не произошел'

    @allure.title("Проверка перехода на главную страницу Яндекса при клике на лого Яндекса")
    def test_click_yandex_logo_go_to_yandex_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        main_page.wait_element(MainPageLocators.logo_yandex)
        driver.switch_to.window(driver.window_handles[1])
        expected_url = Urls.yandex_dzen
        current_url = driver.current_url
        assert expected_url in current_url, 'При клике на лого Яндекса переход на страницу Яндекс Дзен не произошел'

