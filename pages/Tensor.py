from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class TensorHomePage(BasePage):
    """
    Главная страница компании Тензор
    """
    def __init__(self, driver):
        super().__init__(driver)

    power_in_people = (By.XPATH, "//*[text()[contains(.,'Сила в людях')]]")
    more_link = (By.CSS_SELECTOR, '[href="/about"].tensor_ru-Index__link')
    working_images = (By.CSS_SELECTOR, '.tensor_ru-About__block3')

    def open(self):
        """
        Перейти на главную страницу Тензора
        """

        self.driver.get("https://tensor.ru/")

    def verify_working_images(self):
        images = self.driver.find_elements(By.TAG_NAME, 'img')
        same_images_check = []
        for image in images[1:5]:
            size = image.size
            same_images_check.append((size['width'], size['height']))
        assert len(set(same_images_check)) == 1
