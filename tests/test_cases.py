#  Тестовое задание на позицию QA Automation компании Тензор
#  задание: https://cloud.mail.ru/attaches/17092842630329201983%3B0%3B1?folder-id=0&x-email=fizyaaa%40mail.ru&cvg=f

from pages.SbisHomePage import SbisHomePage
from pages.Tensor import TensorHomePage
from pages.SelectRegionMenu import RegionMenu


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
    sbis_page.check_current_url(url=tensor_url)
    # 4
    tensor_page.check_displayed(element_locator=TensorHomePage.power_in_people)
    # 5
    tensor_page.find_element(locator=TensorHomePage.more_link).click()
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
