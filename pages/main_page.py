import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Прокручиваем страницу до Вопросов о важном')
    def scroll_page_down(self):
        self.scroll_to_element(MainPageLocators.QUESTIONS_SECTION)


    @allure.step('Кликаем на вопрос')
    def question_click(self, number):
        self.wait_visibility_of_element(MainPageLocators.QUESTIONS[number])
        self.click_element(MainPageLocators.QUESTIONS[number])

    @allure.step('Узнаем ответ')
    def find_answer(self, number):
        self.wait_visibility_of_element(MainPageLocators.ANSWERS[number])
        return self.get_text_of_element(MainPageLocators.ANSWERS[number])
