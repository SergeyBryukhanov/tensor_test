#  Тестовое задание на позицию QA Automation компании Тензор
#  задание: https://cloud.mail.ru/attaches/17092842630329201983%3B0%3B1?folder-id=0&x-email=fizyaaa%40mail.ru&cvg=f

from pages.SbisHomePage import SbisHomePage
from pages.Tensor import TensorPage
from pages.ListOfPartners import ListOfPartners


def test_case_1(driver):

    tensor_url = "https://tensor.ru/"
    tensor_about_url = 'https://tensor.ru/about'

    sbis_page = SbisHomePage(driver)
    tensor_page = TensorPage(driver)

    # 1
    sbis_page.open()
    sbis_page.find_element(sbis_page.contacts).click()
    # 2
    sbis_page.find_element(sbis_page.tensor_link).click()
    # 3
    sbis_page.switch_windows(1)
    sbis_page.check_current_url(tensor_url)
    # 4
    element = tensor_page.find_element(TensorPage.power_in_people)
    assert element.is_displayed()
    # 5
    element = tensor_page.find_element(TensorPage.more_link)
    element.click()
    sbis_page.check_current_url(tensor_about_url)
    # 6
    tensor_page.verify_working_images(driver)


def test_case_2(driver):
    # 1
    sbis_page = SbisHomePage(driver)
    partners = ListOfPartners(driver)
    sbis_page.open()
    sbis_page.find_element(sbis_page.contacts).click()
    # 2
    region = sbis_page.find_element(sbis_page.region)
    assert region.text == 'Ярославская обл.'
    partners_list = sbis_page.find_element(sbis_page.partners_list)
    assert partners_list.is_displayed()
    # 3
    region.click()
    sbis_page.find_element()
    # 4
    element_3 = sbis_page.find_element()
    assert element_3.text == 'Камчатский край'
    assert driver.current_url == 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'
    element_4 = sbis_page.find_element()
    assert element_4.is_displayed()
    assert 'Петропавловск-Камчатский' in element_4.text
    assert driver.title == 'СБИС Контакты — Камчатский край'
