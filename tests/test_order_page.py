import pytest
import allure
from pages.order_page import OrderPage
from pages.order_page import OrderPageLocators
from sources.data import TestData


class TestOrder:
    @allure.title('Проверка оформления заказа')
    @allure.description('Тестирование оформления заказа из двух разных точек входа')
    @pytest.mark.parametrize('button, data_user', [(OrderPageLocators.ORDER_BUTTON_IN_HEADER, TestData.data_user1),
                                                   (OrderPageLocators.ORDER_BUTTON_IN_MIDDLE, TestData.data_user2)])
    def test_successful_order(self, driver, button, data_user):
        order_page = OrderPage(driver)
        order_page.click_cookie()
        order_page.scroll_to_element(button)
        order_page.click_java(button)
        order_page.fill_form_1(data_user)
        order_page.fill_form_2()
        order_page.confirm_order()
        success = order_page.find_button_status()
        assert success.is_displayed(), "Кнопка Посмотреть статус не отображается"
