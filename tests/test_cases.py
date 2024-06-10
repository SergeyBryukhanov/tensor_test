#  Тестовое задание на позицию QA Automation компании Тензор
#  задание: https://cloud.mail.ru/attaches/17092842630329201983%3B0%3B1?folder-id=0&x-email=fizyaaa%40mail.ru&cvg=f

from pages.SbisHomePage import SbisHomePage
from pages.Tensor import TensorHomePage
from pages.ListOfPartners import ListOfPartners


def test_case_01(driver):

    tensor_url = "https://tensor.ru/"
    tensor_about_url = 'https://tensor.ru/about'

    sbis_page = SbisHomePage(driver)
    tensor_page = TensorHomePage(driver)

    # 1
    sbis_page.open()
    sbis_page.find_element(sbis_page.contacts).click()
    # 2
    sbis_page.find_element(sbis_page.tensor_link).click()
    # 3
    sbis_page.switch_windows(1)
    sbis_page.check_current_url(tensor_url)
    # 4
    element = tensor_page.find_element(TensorHomePage.power_in_people)
    tensor_page.check_displayed(element)
    # 5
    tensor_page.find_element(TensorHomePage.more_link).click()
    sbis_page.check_current_url(tensor_about_url)
    # 6
    tensor_page.verify_working_images()


def test_case_02(driver):

    kamchatskij_kraj_url = 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'
    yar_obl = 'Ярославская обл.'
    kamchatskij_kraj = 'Камчатский край'

    sbis_page = SbisHomePage(driver)
    partners = ListOfPartners(driver)

    # 1
    sbis_page.open()
    sbis_page.find_element(sbis_page.contacts).click()
    # 2
    sbis_page.check_region(yar_obl)
    partners_list = sbis_page.find_element(sbis_page.partners_list)
    sbis_page.check_displayed(partners_list)
    # 3
    sbis_page.find_element(sbis_page.region).click()
    partners.find_region(kamchatskij_kraj)
    # 4
    sbis_page.check_region(kamchatskij_kraj)

    sbis_page.check_current_url(kamchatskij_kraj_url)
    # element_4 = sbis_page.find_element()
    # assert element_4.is_displayed()
    # assert 'Петропавловск-Камчатский' in element_4.text
    assert driver.title == 'СБИС Контакты — Камчатский край'
