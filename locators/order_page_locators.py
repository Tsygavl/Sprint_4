from selenium.webdriver.common.by import By


class OrderPageLocators:
    order_button_header = (By.XPATH, "//button[@class = 'Button_Button__ra12g' and text()='Заказать']")  # Кнопка Заказать в шапке
    order_button_middle = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']")  # Кнопка Заказать внизу
    user_name = (By.XPATH, "//input[contains(@placeholder,'Имя')]")  # Имя
    user_surname = (By.XPATH, "//input[contains(@placeholder, '* Фамилия')]")  # Фамилия
    user_address = (By.XPATH, "//input[contains(@placeholder, '* Адрес: куда привезти заказ')]")  # Адрес
    metro_dropdown = (By.XPATH, "//input[contains(@placeholder, '* Станция метро')]")  # Cтанция метро
    user_phone = (By.XPATH, "//input[contains(@placeholder, '* Телефон: на него позвонит курьер')]")  # Телефон
    next_button = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Далее']")  # Кнопка Далее
    order_date = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")  # Выбор даты заказа
    rental_duration = (By.XPATH, "//div[text()='* Срок аренды']")  # Срок аренды (поле)
    rental_duration_dropdown = (By.XPATH, ".//*[@class='Dropdown-arrow']")  # Дропдаун со сроками аренды
    rental_dropdown_option = {
        1: [By.XPATH, "(//div[@class='Dropdown-option'])[1]"],
        2: [By.XPATH, "(//div[@class='Dropdown-option'])[2]"],
        3: [By.XPATH, "(//div[@class='Dropdown-option'])[3]"],
        4: [By.XPATH, "(//div[@class='Dropdown-option'])[4]"],
        5: [By.XPATH, "(//div[@class='Dropdown-option'])[5]"],
        6: [By.XPATH, "(//div[@class='Dropdown-option'])[6]"],
        7: [By.XPATH, "(//div[@class='Dropdown-option'])[7]"]
    }
    scooter_color_black = (By.ID, 'black')  # Выбор черного самоката
    scooter_color_grey = (By.ID, 'grey')  # Выбор серого самоката
    comments = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")  # Комментарий
    order_button = (By.XPATH, "//button[text()='Назад']/parent::div/button[text()='Заказать']")  # Кнопка Заказать
    back_button = (By.XPATH, "//button[text()='Назад']")  # Кнопка Назад
    confirmation_modal_window = (By.XPATH, "//div[starts-with(text(), 'Хотите')]")  # Модалка подтверждения заказа
    yes_order_button = (By.XPATH, ".//button[text()='Да']")  # Кнопка Да, хочу оформить заказ
    success_order_modal_window = (By.XPATH, "//div[starts-with(text(), 'Заказ')]")  # Модалка успешно созданного заказа
    order_number = (By.XPATH, ".//div[contains(text(),'Номер заказа')]")  # Текст с номером заказа на модалке
    status_button = (By.XPATH, ".//button[text()='Посмотреть статус']")  # Кнопка Посмотреть статус