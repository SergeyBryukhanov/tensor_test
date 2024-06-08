from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from base_page import BasePage


class TensorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    power_in_people = (By.XPATH, "//*[text()[contains(.,'Сила в людях')]]")
    more_link = (By.CSS_SELECTOR, '[href="/about"].tensor_ru-Index__link')
    working_images = (By.CSS_SELECTOR, '.tensor_ru-About__block3')

    def open(self):
        self.driver.get("https://tensor.ru/")

