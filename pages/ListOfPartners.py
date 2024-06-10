from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class ListOfPartners(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    input = (By.TAG_NAME, "input")

    def find_region(self, region_name: str):
        """
        Найти регион через поиск
        :param region_name: название региона
        :return: регион
        """

        return self.find_element(self.input).send_keys(region_name)
