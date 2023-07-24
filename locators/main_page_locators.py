from selenium.webdriver.common.by import By

class MainPageLocators:

    important_questions_header = (By.XPATH, './/div[text()]="Вопросы о важном"')  # Заголовок Вопросы о важном
    important_questions = (By.XPATH, './/*[contains(@id, "accordion__heading-")]')  # Важный вопрос
    important_answers = (By.XPATH, './/*[contains(@id, "accordion__panel-")]/p')  # Важный ответ
    questions_answers_field = [By.XPATH, './/*[@class="accordion"]']  # Поле с вопросами и ответами
    deliver_scooter_for_you = (By.XPATH, './/*[text()[contains(., "Привезём его прямо к вашей")]]')  # Заголовок на главной странице