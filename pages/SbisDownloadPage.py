from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage


class SbisDownloadPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    link = "https://sbis.ru/"

    tab_plugin = (By.XPATH, "//div[text()[contains(.,'СБИС Плагин')]]")
    windows_tab = (By.XPATH, "//span[text()[contains(.,'Windows')]]")
    download_btn = (By.CSS_SELECTOR, '[href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')
