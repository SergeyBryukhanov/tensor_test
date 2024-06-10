from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from base_page import BasePage


class SbisHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    link = "https://sbis.ru/"

    contacts = (By.LINK_TEXT, "Контакты")
    tensor_link = (By.CSS_SELECTOR, "[href='https://tensor.ru/']")
    region = (By.CSS_SELECTOR, '.sbis_ru-Region-Chooser__text')
    partners_list = (By.CSS_SELECTOR, '[data-qa="list"]')

    def open(self):
        self.driver.get(self.link)

