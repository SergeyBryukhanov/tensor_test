from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import requests
import os
from selenium.common import (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException)


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
        :param arrow_down: если True, то сдвинуться вниз; нужно чтобы уведомление сайта о куки не закрывало элемент
        :return: элемент
        """

        element = WebDriverWait(self.driver, timeout=time).until(EC.presence_of_element_located(locator))

        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()

        if arrow_down:
            element.send_keys(Keys.ARROW_DOWN)

        errors = [NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException]
        wait = WebDriverWait(self.driver, timeout=4, poll_frequency=.25, ignored_exceptions=errors)
        wait.until(EC.visibility_of(element))

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
        """
        Получить ссылку из элемента
        :param element: Webdriver element
        :return: URL-адрес
        """
        url = element.get_attribute('href')  # Берём ссылку на скачивание файла
        element_url = requests.get(url, allow_redirects=True)  # Посылаем запрос по ссылке
        assert element_url.status_code == 200  # Проверяем статус запроса
        return element_url

    def save_file(self, file_name, source):
        """
        Сохранить контент файла
        :param file_name: имя, под которым файл сохранится
        :param source: источник для скачивания файла
        """

        with open(file_name, mode="wb") as file:
            file.write(source.content)

    def check_file_saved(self, file_path: str):
        """
        Проверить сохранён ли файл
        :param file_path: путь до файла
        """

        assert os.path.isfile(file_path)

    def check_file_size(self, file_path: str, file_size: str):
        """
        Проверить размер файла
        :param file_path: путь до файла
        :param file_size: размер для сравнения
        """

        saved_file_size = str(round((os.path.getsize(file_path) / 1024 / 1024), 2))  # Вычисляем размер файла в МБ
        assert file_size == saved_file_size
