import allure
from locators.main_page_locators import MainPageLocators as Lm
from locators.order_page_locators import OrderPageLocators as Lo
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Клик на вопрос")
    def click_for_question(self, question_index):
        base_page = BasePage(self.driver)
        list_of_questions = base_page.find_elements(Lm.important_questions)
        base_page.wait_element(Lm.important_questions)
        list_of_questions[question_index].click()

    @allure.step("Клик на лого Яндекса")
    def click_yandex_logo(self):
        self.click_element(Lm.logo_yandex)

    @allure.step("Клик на лого Самоката")
    def click_scooter_logo(self):
        self.click_element(Lm.logo_scooter)

    @allure.step("Клик на кнопку 'Заказать' в шапке")
    def click_order_button_header(self):
        self.click_element(Lo.order_button_header)

    @allure.step("Нажимаем на кнопку 'Заказать' в центре главной страницы")
    def click_order_button_middle(self):
        self.click_element(Lo.order_button_middle)
