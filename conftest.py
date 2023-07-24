import pytest
from data import Urls
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Urls.samokat_main_page)
    yield driver

    driver.quit()