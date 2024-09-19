from selenium.webdriver.common.by import By


class BasePageLocators:
    COOKIE = By.XPATH, "//button[contains(@class, 'App_CookieButton')]"
    LINK_SCOOTER = By.XPATH, "//a[@href='/']"
    HOME_HEADER = By.XPATH, "//div[contains(@class, 'Home_Header')]"
    LINK_YANDEX = By.XPATH, "//a[@href='//yandex.ru']"
    LOGO_DZEN = By.XPATH, "//a[contains(@class, 'dzen-layout--desktop-base-header')]"
