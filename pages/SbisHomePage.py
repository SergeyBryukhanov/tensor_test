from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SbisHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    link = "https://sbis.ru/"

    contacts = (By.LINK_TEXT, "Контакты")
    tensor_link = (By.CSS_SELECTOR, "[href='https://tensor.ru/']")
    region = (By.CSS_SELECTOR, '.sbis_ru-Region-Chooser__text')
    partners_list = (By.CSS_SELECTOR, '[data-qa="list"]')
    footer_dl = (By.CSS_SELECTOR, '[href="/download"]')

    def open(self):
        """
        Открыть страницу
        """

        self.driver.get(self.link)

    def check_region(self, region_name: str):
        """
        Проверить выбранный регион
        :param region_name: название региона
        """

        region = self.find_element(self.region)
        assert region.text == region_name  # Редко регион выбирается неверно, можно добавить обработку такого исхода

    def check_partners_region(self, partner_text: str):
        """
        Проверить список партнеров текущего региона
        :param partner_text: партнер
        """

        partners_list = self.find_element(self.partners_list)
        assert partner_text in partners_list.text

    def check_title(self, title: str):
        """
        Проверить название сайта
        :param title:название сайта
        """

        assert self.driver.title == title
