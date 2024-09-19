import allure
from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators
from locators.order_page_locators import OrderPageLocators


class TestLogo:
    @allure.title('Проверка перехода на главную страницу при клике на лого Самокат')
    def test_logo_scooter(self, driver):
        logo = BasePage(driver)
        logo.find_element(OrderPageLocators.ORDER_BUTTON_IN_HEADER)
        logo.click_element(OrderPageLocators.ORDER_BUTTON_IN_HEADER)
        logo.find_element(BasePageLocators.LINK_SCOOTER)
        logo.click_element(BasePageLocators.LINK_SCOOTER)
        home = logo.find_element(BasePageLocators.HOME_HEADER)
        assert home.is_displayed(), "Переход на главную страницу не произошел"

    @allure.title('Проверка открытия в новом окне Дзена при клике на лого Яндекса')
    def test_logo_yandex(self, driver):
        logo_ya = BasePage(driver)
        logo_ya.find_element(BasePageLocators.LINK_YANDEX)
        logo_ya.click_element(BasePageLocators.LINK_YANDEX)
        logo_ya.switch_to_next_tab()
        dzen = logo_ya.find_element(BasePageLocators.LOGO_DZEN)
        assert dzen.is_displayed(), "Переход на страницу Дзена не произошел"
