from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTIONS_SECTION = By.XPATH, "//div[contains(@class, 'Home_FourPart')]"
    QUESTIONS = {
        1 : (By.ID, 'accordion__heading-0'),
        2 : (By.ID, 'accordion__heading-1'),
        3 : (By.ID, 'accordion__heading-2'),
        4 : (By.ID, 'accordion__heading-3'),
        5 : (By.ID, 'accordion__heading-4'),
        6 : (By.ID, 'accordion__heading-5'),
        7 : (By.ID, 'accordion__heading-6'),
        8 : (By.ID, 'accordion__heading-7')
    }
    ANSWERS = {
        1 : (By.XPATH, "//div[@id='accordion__panel-0']/p"),
        2 : (By.XPATH, "//div[@id='accordion__panel-1']/p"),
        3 : (By.XPATH, "//div[@id='accordion__panel-2']/p"),
        4 : (By.XPATH, "//div[@id='accordion__panel-3']/p"),
        5 : (By.XPATH, "//div[@id='accordion__panel-4']/p"),
        6 : (By.XPATH, "//div[@id='accordion__panel-5']/p"),
        7 : (By.XPATH, "//div[@id='accordion__panel-6']/p"),
        8 : (By.XPATH, "//div[@id='accordion__panel-7']/p"),
    }
