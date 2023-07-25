import allure
from selenium.webdriver.common.keys import Keys
from pages.main_page import MainPage
from locators.order_page_locators import OrderPageLocators as Lo


class OrderPage(MainPage):


    @allure.step("Заполнение поля Имя")
    def input_name(self, name):
        self.send_key(Lo.user_name, name)

    @allure.step("Заполнение поля 'Фамилия'")
    def input_surname(self, surname):
        self.send_key(Lo.user_surname, surname)

    @allure.step("Заполняем поле 'Адрес'")
    def input_address(self, address):
        self.send_key(Lo.user_address, address)

    @allure.step("Выбор станции метро")
    def choose_subway_station(self, station):
        self.click_element(Lo.metro_dropdown)
        self.send_key(Lo.metro_dropdown, station)
        self.send_key(Lo.metro_dropdown, Keys.ARROW_DOWN + Keys.ENTER)

    @allure.step("Заполняем поле 'Телефон'")
    def input_user_phone(self, phone):
        self.send_key(Lo.user_phone, phone)

    @allure.step("Нажимаем 'Далее'")
    def click_next_button(self):
        self.click_element(Lo.next_button)

    @allure.step("Выбираем дату")
    def choose_order_date(self, date):
        self.send_key(Lo.order_date, date)
        self.send_key(Lo.order_date, Keys.ENTER)

    @allure.step("Выбираем срок аренды")
    def choose_rental_duration(self, period):
        self.click_element(Lo.rental_duration_dropdown)
        self.click_element(Lo.rental_dropdown_option[period])

    @allure.step("Выбираем цвет самоката")
    def choose_scooter_color(self, black_color, grey_color):
        if black_color:
            self.click_element(Lo.scooter_color_black)
        if grey_color:
            self.click_element(Lo.scooter_color_grey)

    @allure.step("Пишем комментарий")
    def write_comment(self, comment):
        self.send_key(Lo.comments, comment)

    @allure.step("Нажимаем 'Заказать'")
    def click_order_button(self):
        self.click_element(Lo.order_button)

    @allure.step("Подтверждение заказа")
    def confirm_order(self):
        self.click_element(Lo.yes_order_button)

    @allure.step("Оформляем заказ")
    def make_order(self, user):
        self.input_name(user.name)
        self.input_surname(user.surname)
        self.input_address(user.address)
        self.choose_subway_station(user.station)
        self.input_user_phone(user.phone)
        self.click_next_button()
        self.choose_order_date(user.date)
        self.choose_rental_duration(user.period)
        self.choose_scooter_color(user.black_color, user.grey_color)
        self.write_comment(user.comment)
        self.click_order_button()
        self.confirm_order()