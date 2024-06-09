import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.set_window_position(2000, 0)
    driver.maximize_window()

    yield driver

    driver.quit()
