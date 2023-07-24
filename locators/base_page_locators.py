from selenium.webdriver.common.by import By


class BasePageLocators:
    cookies_accept = (By.XPATH, './/button[text()="да все привыкли"]') # Кнопка принятие куки
    order_status_button = (By.XPATH, './/button[text()="Статус заказа"]') # Кнопка узнать статус
    order_button = (By.XPATH, './/button[text()="Заказать"]') #Кнопка "заказать"
    logo_yandex = (By.XPATH, './/img[@alt="Yandex"]') # Логотип яндекса
    logo_scooter = (By.XPATH, './/img[@alt="Scooter"]') # Логотип скутера
    yandex_search = (By.XPATH, './/iframe[@aria-label="Поиск Яндекса"]') # строка поиска в Яндексе
    logo_dzen = (By.XPATH, "//a[@class='desktop-base-header__logoLink-aE']")



