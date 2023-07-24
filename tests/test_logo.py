import allure
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from data import Urls


class TestLogo:

    @allure.title("Проверка перехода на главную страницу Самоката при клике на лого Самоката")
    def test_click_scooter_logo_go_to_samokat_page(self, driver):
        base_page = BasePage(driver)
        driver.get(Urls.samokat_order_page)
        base_page.click_scooter_logo()
        assert base_page.find_element(MainPageLocators.deliver_scooter_for_you), \
            'При клике на лого Самоката переход на главную страницу Самоката не произошел'

    @allure.title("Проверка перехода на главную страницу Яндекса при клике на лого Яндекса")
    def test_click_yandex_logo_go_to_yandex_page(self, driver):
        base_page = BasePage(driver)
        base_page.click_yandex_logo()
        #base_page.wait_element(BasePageLocators.logo_yandex)
        driver.switch_to.window(driver.window_handles[1])
        assert base_page.find_element(BasePageLocators.logo_dzen), \
            'При клике на лого Яндекса переход на главную страницу Яндекса не произошел'
        # и так пробовал assert driver.current_url == Urls.yandex_dzen без wait_element все равно не идет блин
        # и ждал строку яндекса yandex_search
