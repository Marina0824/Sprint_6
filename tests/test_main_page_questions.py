import pytest
import allure
from pages.main_page import MainPage
from sources.data import TestData


class TestQuestions:
    driver = None
    @allure.title('Проверка вопросов и ответов')
    @allure.description('Тестирование соответствия ответов вопросам')
    @pytest.mark.parametrize('number, expected_answer', TestData.expected_answer)
    def test_questions(self, driver, number, expected_answer):
        main_page = MainPage(driver)
        main_page.scroll_page_down()
        main_page.question_click(number)
        answer = main_page.find_answer(number)
        assert answer == expected_answer, "Полученный ответ не соответствует ожидаемому"
