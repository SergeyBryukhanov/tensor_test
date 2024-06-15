from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import requests


class BasePage:
    """
    Базовый класс для страниц
    """

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10, arrow_down=False):
        """
        Найти элемент и проскролить до него вниз по странице
        :param locator: локатор элемента
        :param time: время ожидания
        :param arrow_down: если True, то сдвинуться вниз, нужно чтобы уведомление браузера о куки не закрывало элемент
        :return: элемент
        """

        element = WebDriverWait(self.driver, timeout=time).until(EC.presence_of_element_located(locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()
        if arrow_down:
            element.send_keys(Keys.ARROW_DOWN)
            sleep(0.2)
        return element

    def switch_windows(self, window: int):
        """
        Переключиться на другое окно браузера
        :param window: номер окна браузера(нумерация с нуля)
        """
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[window])

    def check_current_url(self, url: str):
        """
        Проверить URL текущей страницы
        :param url: URL для сравнения с текущим
        """

        assert self.driver.current_url == url

    def check_displayed(self, element_locator):
        """
        Проверить отображение элемента
        :param element_locator: локатор элемента
        """

        element = self.find_element(element_locator)
        assert element.is_displayed()

    def get_url_link(self, element):
        url = element.get_attribute('href')  # Берём ссылку на скачивание файла
        response = requests.get(url, allow_redirects=True)  # Посылаем запрос по ссылке
        assert response.status_code == 200  # Проверяем статус запроса
        return response

    def save_file(self, file_name, source):
        """
        Сохранить контент файла
        :param file_name: имя, под которым файл сохранится
        :param source: источник для скачивания файла
        """

        with open(file_name, mode="wb") as file:
            file.write(source.content)

    def highlight(self, element):
        """
        Подсветить красной рамкой элемент
        :param element: Webdriver элемент
        """

        element._parent.execute_script(script="arguments[0].set.border='2px solid red');")
