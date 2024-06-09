from SbisHomePage import SbisHomePage
from time import sleep
from selenium import webdriver
from Tensor import TensorPage
from ListOfPartners import ListOfPartners
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_case_1(driver):
    # 1
    sbis_page = SbisHomePage(driver)
    tensor_page = TensorPage(driver)
    sbis_page.open()
    sbis_page.find_element(sbis_page.contacts).click()
    # 2
    sbis_page.find_element(sbis_page.tensor_link).click()
    # 3
    sbis_page.switch_windows(1)
    assert driver.current_url == "https://tensor.ru/"
    # 4
    element = tensor_page.find_element(TensorPage.power_in_people)
    assert element.is_displayed()
    # 5
    element = tensor_page.find_element(TensorPage.more_link)
    element.click()
    assert driver.current_url == 'https://tensor.ru/about'
    # 6
    tensor_page.find_element(TensorPage.working_images)
    images = sbis_page.find_images()
    same_images_check = []
    for image in images[1:5]:
        size = image.size
        same_images_check.append((size['width'], size['height']))
    assert len(set(same_images_check)) == 1


def test_case_2(driver):
    # 1
    sbis_page = SbisHomePage(driver)
    partners = ListOfPartners(driver)
    sbis_page.open()
    sleep(2)
    sbis_page.find_element(sbis_page.contacts).click()
    # 2
    region = sbis_page.find_element(sbis_page.region)
    assert region.text == 'Ярославская обл.'
    partners_list = sbis_page.find_element(sbis_page.partners_list)
    assert partners_list.is_displayed()
    # 3
    region.click()
    sbis_page.find_element()
    sleep(1)
    # 4
    element_3 = sbis_page.find_element()
    assert element_3.text == 'Камчатский край'
    assert driver.current_url == 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'
    element_4 = sbis_page.find_element()
    assert element_4.is_displayed()
    assert 'Петропавловск-Камчатский' in element_4.text
    sleep(1)
    assert driver.title == 'СБИС Контакты — Камчатский край'
