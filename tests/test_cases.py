#  Тестовое задание на позицию QA Automation компании Тензор
#  задание: https://cloud.mail.ru/public/2WPt/aYxTGDtSx

import os
import re

from pages.SbisHomePage import SbisHomePage
from pages.Tensor import TensorHomePage
from pages.SelectRegionMenu import RegionMenu
from pages.SbisDownloadPage import SbisDownloadPage


class TestCases:

    def test_case_01(self, driver):
        """
        Первый тест-кейс, переход по страницам сайта Тензор
        """

        tensor_url = "https://tensor.ru/"
        tensor_about_url = 'https://tensor.ru/about'

        sbis_page = SbisHomePage(driver)
        tensor_page = TensorHomePage(driver)

        # 1
        sbis_page.open()
        sbis_page.find_element(locator=sbis_page.contacts).click()

        # 2
        sbis_page.find_element(locator=sbis_page.tensor_link).click()

        # 3
        sbis_page.switch_windows(window=1)
        sbis_page.check_current_url(url=tensor_url)

        # 4
        tensor_page.check_displayed(element_locator=TensorHomePage.power_in_people)

        # 5
        more_link = tensor_page.find_element(locator=TensorHomePage.more_link, arrow_down=True)
        more_link.click()
        sbis_page.check_current_url(url=tensor_about_url)

        # 6
        tensor_page.verify_working_images()

    def test_case_02(self, driver):
        """
        Второй тест-кейс, смена региона и проверка списка партнеров
        """

        kamchatskij_kraj_url = 'https://saby.ru/contacts/41-kamchatskij-kraj?tab=clients'

        yar_obl = 'Ярославская обл.'
        kamchatskij_kraj = 'Камчатский край'
        petropavlovsk = 'Петропавловск-Камчатский'
        kamchatskij_kraj_title = 'Saby Контакты — Камчатский край'

        sbis_page = SbisHomePage(driver)
        partners = RegionMenu(driver)

        # 1
        sbis_page.open()
        sbis_page.find_element(locator=sbis_page.contacts).click()

        # 2
        sbis_page.check_region(region_name=yar_obl)
        sbis_page.check_displayed(element_locator=sbis_page.partners_list)

        # 3
        sbis_page.find_element(locator=sbis_page.region).click()
        partners.select_region(region_name=kamchatskij_kraj)

        # 4
        sbis_page.check_region(region_name=kamchatskij_kraj)
        sbis_page.check_partners_region(partner_text=petropavlovsk)
        sbis_page.check_current_url(url=kamchatskij_kraj_url)
        sbis_page.check_title(title=kamchatskij_kraj_title)

    def test_case_03(self, driver):
        """
        Третий тест-кейс, проверка скачивания плагина
        """

        sbis_page = SbisHomePage(driver)
        sbis_dl = SbisDownloadPage(driver)

        file_name = "sbis_plugin.exe"
        dir_path = os.path.abspath(os.path.dirname(__file__))  # Путь до локальной директории
        file_path = os.path.join(dir_path, file_name)  # Добавляем к пути имя файла

        # 1
        sbis_page.open()

        # 2
        element = sbis_page.find_element(sbis_page.footer_dl, arrow_down=True)
        element.click()

        # 3
        sbis_dl.find_element(sbis_dl.tab_plugin).click()
        sbis_dl.find_element(sbis_dl.windows_tab).click()
        download_btn = sbis_dl.find_element(sbis_dl.download_btn)
        source = sbis_dl.get_url_link(download_btn)
        sbis_dl.save_file(file_path=file_path, source=source)

        # 4
        sbis_dl.check_file_saved(file_path)

        # 5
        file_size = re.findall(r'\d+\.\d+', download_btn.text)[0]
        sbis_dl.check_file_size(file_path=file_path, file_size=file_size)

        # Удалить файл после теста
        os.remove(path=file_path)
