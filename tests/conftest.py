import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    """
    Фикстура для работы с браузера
    """

    driver = webdriver.Chrome()
    driver.set_window_position(2000, 0)  # Переключение браузера на дополнительный монитор
    driver.maximize_window()

    yield driver

    driver.quit()
