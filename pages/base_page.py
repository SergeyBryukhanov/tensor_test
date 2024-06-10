from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    """
    Базовый класс для страниц
    """

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        """
        Найти элемент и проскролить до него вниз по странице
        :param locator: локатор элемента
        :param time: время ожидания
        :return: элемент
        """

        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.scroll_by_amount(delta_y=200, delta_x=0)
        actions.perform()
        return element

    def switch_windows(self, number: int):
        """
        Переключиться на другое окно браузера
        :param number: номер окна браузера(нумерация с нуля)
        """
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[number])

    def check_current_url(self, url: str):
        """
        Проверить URL текущей страницы
        :param url: URL для сравнения с текущим
        """

        assert self.driver.current_url == url

    def check_displayed(self, element):
        """
        Проверить отображение элемента
        :param element: локатор элемента
        """

        assert element.is_displayed()
