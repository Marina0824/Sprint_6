import pytest
from selenium import webdriver


URL = 'https://qa-scooter.praktikum-services.ru/'

@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Firefox()
    driver.get(URL)
    yield driver
    driver.quit()
