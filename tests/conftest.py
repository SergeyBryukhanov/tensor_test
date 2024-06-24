import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def driver():
    """
    Фикстура для работы с браузера
    """

    driver = webdriver.Chrome()
    driver.set_window_position(2000, 0)  # Переключить браузер на дополнительный монитор
    driver.maximize_window()

    yield driver

    driver.quit()
