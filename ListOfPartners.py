from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from base_page import BasePage


class ListOfPartners(BasePage):
    def __init__(self, driver):
        super().__init__(driver)



