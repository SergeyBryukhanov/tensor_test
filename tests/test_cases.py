#  Тестовое задание на позицию QA Automation компании Тензор
#  задание: https://cloud.mail.ru/attaches/17092842630329201983%3B0%3B1?folder-id=0&x-email=fizyaaa%40mail.ru&cvg=f

from time import sleep
from selenium.webdriver import Keys
from pages.SbisHomePage import SbisHomePage
from pages.Tensor import TensorHomePage
from pages.SelectRegionMenu import RegionMenu
from pages.SbisDownloadPage import SbisDownloadPage
import os
import requests
from selenium.webdriver.common.by import By


def test_case_01(driver):
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
    a = driver.current_url
    sbis_page.check_current_url(url=tensor_url)
    # 4
    tensor_page.check_displayed(element_locator=TensorHomePage.power_in_people)
    # 5
    more_link = tensor_page.find_element(locator=TensorHomePage.more_link, arrow_down=True)
    more_link.click()
    sbis_page.check_current_url(url=tensor_about_url)
    # 6
    tensor_page.verify_working_images()


def test_case_02(driver):
    """
    Второй тест-кейс, смена региона и проверка списка партнеров
    """

    kamchatskij_kraj_url = 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'
    yar_obl = 'Ярославская обл.'
    kamchatskij_kraj = 'Камчатский край'
    petropavlovsk = 'Петропавловск-Камчатский'
    kamchatskij_kraj_title = 'СБИС Контакты — Камчатский край'

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


def test_case_03(driver):
    """
    Третий тест-кейс, проверка скачивания плагина
    """

    sbis_page = SbisHomePage(driver)
    sbis_dl = SbisDownloadPage(driver)

    file_name = "sbis_plugin.exe"
    dir_path = os.path.dirname(os.path.realpath(__file__))  # Путь локальной директории
    dir_path += '\{0}'.format(file_name)

    sbis_page.open()  # Переход на sbis.ru
    element = sbis_page.find_element(sbis_page.footer_dl)  # Находим кнопку "Скачать локальные версии"
    element.send_keys(Keys.END)
    element.click()

    sbis_dl.find_element(sbis_dl.tab_plugin).click()
    sbis_dl.find_element(sbis_dl.windows_tab).click()
    download_btn = sbis_dl.find_element(sbis_dl.download_btn)
    response = sbis_dl.get_url_link(download_btn)

    sbis_dl.save_file(file_name=file_name, source=response)
    file_size = round((os.path.getsize(dir_path) / 1024 / 1024), 2)  # Вычисляем размер файла в МБ
    print(f'\n{file_size} МБ')
    assert os.path.exists(dir_path) == True
    os.remove(path=dir_path)
