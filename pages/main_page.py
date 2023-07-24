import allure
from locators.main_page_locators import MainPageLocators as Lm
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Клик на вопрос")
    def check_answers_for_important_questions(self, question_index):
        base_page = BasePage(self.driver)
        list_of_questions = base_page.find_elements(Lm.important_questions)
        base_page.wait_element(Lm.important_questions)
        list_of_questions[question_index].click()
