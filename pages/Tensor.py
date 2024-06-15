from selenium.webdriver.common.by import By
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
        """
        Проверить, что все изображения блока 'Работаем' одного размера
        """

        images = self.driver.find_elements(By.CSS_SELECTOR, '.s-Grid-col img')
        same_images_check = [(image.size['width'], image.size['height']) for image in images[:4]]
        assert len(set(same_images_check)) == 1

