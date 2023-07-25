import allure
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
        self.click_element(Lm.cookies_accept)

    def send_key(self, locator, key):
        return self.find_element(locator).send_keys(key)

    def get_element_text(self, locator):
        return self.find_element(locator).text
