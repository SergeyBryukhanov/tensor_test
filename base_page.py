from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        """
        Найти элемент и проскролить до него вниз по странице
        :param locator: локатор элемента
        :param time: время ожидания
        :return:
        """

        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.scroll_by_amount(delta_y=200, delta_x=0)
        actions.perform()
        return element

    def move_to(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        return actions.perform()

    def switch_windows(self, number):
        windows = self.driver.window_handles
        return self.driver.switch_to.window(windows[number])

