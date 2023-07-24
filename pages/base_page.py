import allure
from locators.base_page_locators import BasePageLocators as Lb
from locators.main_page_locators import MainPageLocators as Lm
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator):
        return WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(locator))

    def wait_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_any_elements_located(locator))

    def click_element(self, locator):
        self.find_element(locator).click()

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Принять куки")
    def accept_cookies(self):
        self.click_element(Lb.cookies_accept)

    @allure.step("Клик на лого Яндекса")
    def click_yandex_logo(self):
        self.click_element(Lb.logo_yandex)

    @allure.step("Клик на лого Самоката")
    def click_scooter_logo(self):
        self.click_element(Lb.logo_scooter)


        