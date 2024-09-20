import allure
from pages.main_page import MainPage


class TestLogo:
    @allure.title('Проверка перехода на главную страницу при клике на лого Самокат')
    def test_logo_scooter(self, driver):
        logo = MainPage(driver)
        logo.find_order_button_in_header()
        logo.click_order_button_in_header()
        logo.find_logo_scooter()
        logo.click_logo_scooter()
        home = logo.find_home_header()
        assert home.is_displayed(), "Переход на главную страницу не произошел"

    @allure.title('Проверка открытия в новом окне Дзена при клике на лого Яндекса')
    def test_logo_yandex(self, driver):
        logo_ya = MainPage(driver)
        logo_ya.find_logo_yandex()
        logo_ya.click_logo_yandex()
        logo_ya.switch_to_next_tab()
        dzen = logo_ya.find_logo_dzen()
        assert dzen.is_displayed(), "Переход на страницу Дзена не произошел"
