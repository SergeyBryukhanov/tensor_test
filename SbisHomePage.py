from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from base_page import BasePage


class Locators:

    Region = (By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
    Spisok_partnerov = (By.XPATH, '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]')
    Kamchtskij_krai = (By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span')


class SbisHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    contacts = (By.LINK_TEXT, "Контакты")
    tensor_link = (By.CSS_SELECTOR, "[href='https://tensor.ru/']")

    def open(self):
        self.driver.get("https://sbis.ru/")
