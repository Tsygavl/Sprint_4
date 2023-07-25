from selenium.webdriver.common.by import By

class MainPageLocators:

    cookies_accept = (By.XPATH, './/button[text()="да все привыкли"]') # Кнопка принятие куки
    order_status_button = (By.XPATH, './/button[text()="Статус заказа"]') # Кнопка узнать статус
    order_button = (By.XPATH, './/button[text()="Заказать"]') #Кнопка "заказать"
    logo_yandex = (By.XPATH, './/img[@alt="Yandex"]') # Логотип яндекса
    logo_scooter = (By.XPATH, './/img[@alt="Scooter"]') # Логотип скутера
    yandex_search = (By.XPATH, './/iframe[@aria-label="Поиск Яндекса"]') # строка поиска в Яндексе
    logo_dzen = (By.XPATH, "//a[@class='desktop-base-header__logoLink-aE']")
    important_questions_header = (By.XPATH, './/div[text()]="Вопросы о важном"')  # Заголовок Вопросы о важном
    important_questions = (By.XPATH, './/*[contains(@id, "accordion__heading-")]')  # Важный вопрос
    important_answers = (By.XPATH, './/*[contains(@id, "accordion__panel-")]/p')  # Важный ответ
    questions_answers_field = [By.XPATH, './/*[@class="accordion"]']  # Поле с вопросами и ответами
    deliver_scooter_for_you = (By.XPATH, './/*[text()[contains(., "Привезём его прямо к вашей")]]')  # Заголовок на главной странице