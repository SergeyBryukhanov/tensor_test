from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SbisDownloadPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    link = "https://sbis.ru/"

    tab_plugin = (By.XPATH, "//div[text()[contains(.,'Saby Plugin')]]")
    windows_tab = (By.XPATH, "//span[text()[contains(.,'Windows')]]")
    download_btn = (By.CSS_SELECTOR, '[href="https://update.saby.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]')