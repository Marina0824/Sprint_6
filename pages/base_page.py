import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    def enter_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))

    def get_text_of_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Куки!')
    def click_cookie(self):
        self.wait_visibility_of_element(BasePageLocators.COOKIE)
        self.click_element(BasePageLocators.COOKIE)

    def click_java(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Переход на другую вкладку')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
