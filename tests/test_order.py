import pytest
import allure
from locators.order_page_locators import OrderPageLocators as Lo
from pages.order_page import OrderPage
from data import user_1, user_2


class TestOrder:

    @allure.title("Проверка оформления заказа кнопкой Заказать в хэдере")
    @pytest.mark.parametrize('user', [user_1, user_2])
    def test_order_by_click_header_order_button(self, driver, user):
        order_page = OrderPage(driver)
        order_page.accept_cookies()
        order_page.click_order_button_header()
        order_page.make_order(user)
        order_text = order_page.get_element_text(Lo.success_order_modal_window)
        assert "Заказ оформлен" in order_text, 'Ошибка во время оформления заказа'


    @allure.title("Проверка оформления заказа кнопкой Заказать в центре страницы")
    @pytest.mark.parametrize('user', [user_1, user_2])
    def test_order_by_click_order_button_middle(self, driver, user):
        order_page = OrderPage(driver)
        order_page.accept_cookies()
        order_page.click_order_button_middle()
        order_page.make_order(user)
        order_text = order_page.get_element_text(Lo.success_order_modal_window)
        assert "Заказ оформлен" in order_text, "Ошибка во время оформления заказа"
