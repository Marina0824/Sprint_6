import allure
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Прокручиваем страницу до Вопросов о важном')
    def scroll_page_down(self):
        self.scroll_to_element(MainPageLocators.QUESTIONS_SECTION)

    @allure.step('Кликаем на вопрос')
    def question_click(self, number):
        self.find_element(MainPageLocators.QUESTIONS[number])
        self.click_element(MainPageLocators.QUESTIONS[number])

    @allure.step('Узнаем ответ')
    def find_answer(self, number):
        self.find_element(MainPageLocators.ANSWERS[number])
        return self.get_text_of_element(MainPageLocators.ANSWERS[number])

    @allure.step('Находим в хедере кнопку Заказать')
    def find_order_button_in_header(self):
        self.find_element(OrderPageLocators.ORDER_BUTTON_IN_HEADER)

    @allure.step('Кликаем в хедере на кнопку Заказать')
    def click_order_button_in_header(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON_IN_HEADER)

    @allure.step('Находим лого Самокат')
    def find_logo_scooter(self):
        self.find_element(BasePageLocators.LINK_SCOOTER)

    @allure.step('Кликаем на лого Самокат')
    def click_logo_scooter(self):
        self.click_element(BasePageLocators.LINK_SCOOTER)

    @allure.step('Находим хедер Самокат на пару дней')
    def find_home_header(self):
        self.find_element(BasePageLocators.HOME_HEADER)

    @allure.step('Находим хедер Самокат на пару дней')
    def find_home_header(self):
        return self.find_element(BasePageLocators.HOME_HEADER)

    @allure.step('Находим лого Яндекс')
    def find_logo_yandex(self):
        self.find_element(BasePageLocators.LINK_YANDEX)

    @allure.step('Кликаем на лого Яндекс')
    def click_logo_yandex(self):
        self.click_element(BasePageLocators.LINK_YANDEX)

    @allure.step('Находим лого Дзен')
    def find_logo_dzen(self):
        return self.find_element(BasePageLocators.LOGO_DZEN)
