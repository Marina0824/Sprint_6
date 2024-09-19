import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Заполнение первой формы')
    def fill_form_1(self, data_user):
        self.wait_visibility_of_element(OrderPageLocators.FIELD_NAME)
        self.enter_text(OrderPageLocators.FIELD_NAME, data_user[0])
        self.enter_text(OrderPageLocators.FIELD_SURNAME, data_user[1])
        self.enter_text(OrderPageLocators.FIELD_ADDRESS, data_user[2])
        metro = data_user[3]
        self.enter_text(OrderPageLocators.FIELD_METRO, metro)
        self.click_element(OrderPageLocators.get_metro_locator(metro))
        self.enter_text(OrderPageLocators.FIELD_PHONE, data_user[4])
        self.click_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Заполнение второй формы')
    def fill_form_2(self):
        self.wait_visibility_of_element(OrderPageLocators.FIELD_DATA)
        self.click_element(OrderPageLocators.FIELD_DATA)
        self.wait_visibility_of_element(OrderPageLocators.CALENDAR)
        self.click_element(OrderPageLocators.CHOOSEN_DAY)
        self.click_element(OrderPageLocators.FIELD_RENTAL_PERIOD)
        self.wait_visibility_of_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_element(OrderPageLocators.QUANTITY_DAYS)
        self.click_element(OrderPageLocators.ORDER_BUTTON_DOWN)

    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        self.wait_visibility_of_element(OrderPageLocators.CONFIRM_ORDER)
        self.click_element(OrderPageLocators.CONFIRM_ORDER)
        self.wait_visibility_of_element(OrderPageLocators.STATUS)
