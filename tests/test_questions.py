import pytest
import allure
from locators.main_page_locators import MainPageLocators as Lm
from pages.main_page import MainPage
from data import QuestionsAnswers


class TestQuestions:

    @allure.title("Проверка соответствия вопросов и ответов")
    @pytest.mark.parametrize('question_index', [i for i in range(8)])
    def test_questions_and_answers(self, question_index, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.scroll_down()
        main_page.click_for_question(question_index)
        actual_result = main_page.get_element_text(Lm.important_answers)[question_index]
        expected_result = QuestionsAnswers.questions_and_answers[main_page.get_element_text(
            Lm.important_questions)[question_index]]
        assert actual_result == expected_result, 'Ответ не соответствует вопросу'