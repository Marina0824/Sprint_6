from selenium.webdriver.common.by import By


class OrderPageLocators:
    FIELD_NAME = By.XPATH, "//input[@placeholder='* Имя']"
    FIELD_SURNAME = By.XPATH, "//input[@placeholder='* Фамилия']"
    FIELD_ADDRESS = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    FIELD_METRO = By.XPATH, "//input[@placeholder='* Станция метро']"
    FIELD_PHONE = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    BUTTON_NEXT = By.XPATH, "//button[text()='Далее']"

    FIELD_DATA = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    CALENDAR = By.XPATH, "//div[@class='react-datepicker-popper']"
    CHOOSEN_DAY = By.XPATH, "//div[contains(@class, 'day--024')]"
    FIELD_RENTAL_PERIOD = By.XPATH, "//div[@class='Dropdown-placeholder']"
    RENTAL_PERIOD = By.XPATH, "//div[@class='Dropdown-menu']"
    QUANTITY_DAYS = By.XPATH, "//div[@class='Dropdown-option' and text()='двое суток']"
    ORDER_BUTTON_DOWN = By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']"

    CONFIRM_ORDER = By.XPATH, "//button[text()='Да']"
    STATUS = By.XPATH, "//button[text()='Посмотреть статус']"

    @staticmethod
    def get_metro_locator(metro):
        return By.XPATH, f"//*[@class='select-search__select']//*[text()='{metro}']"
