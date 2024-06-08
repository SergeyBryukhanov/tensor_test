from SbisHomePage import Locators
from SbisHomePage import SbisHomePage
from time import sleep
import pytest
from selenium import webdriver
from Tensor import TensorPage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_case_1(driver):
    #1
    sbis_page = SbisHomePage(driver)
    tensor_page = TensorPage(driver)
    sbis_page.open()
    sleep(2)
    sbis_page.find_element(sbis_page.contacts).click()
    #2
    sbis_page.find_element(sbis_page.tensor_link).click()
    #3
    sbis_page.switch_windows(1)
    assert driver.current_url == "https://tensor.ru/"
    #4
    element = tensor_page.find_element(TensorPage.power_in_people)
    assert element.is_displayed()
    #5
    element = tensor_page.find_element(TensorPage.more_link)
    element.click()
    assert driver.current_url == 'https://tensor.ru/about'
    #6
    tensor_page.find_element(TensorPage.working_images)
    images = driver.find_elements(By.TAG_NAME, 'img')
    same_images_check = []
    for image in images[1:5]:
            try:
                size = image.size
                same_images_check.append((size['width'], size['height']))
            except:
                print('image could be hidden')
    assert len(set(same_images_check)) == 1

def test_case_2(browser):
    #1
    Page = SbisHomePage(browser)
    Page.open_sbis()
    sleep(2)
    Page.find_and_click(Locators.Contacts)
    #2
    element_1 = Page.element_to_find(Locators.Region)
    assert element_1.text == 'Ярославская обл.'
    element_2 = Page.element_to_find(Locators.Spisok_partnerov)
    assert element_2.is_displayed()
    #3
    element_1.click()
    Page.find_and_click(Locators.Kamchtskij_krai)
    sleep(1)
    #4
    element_3 = Page.element_to_find(Locators.Region)
    assert element_3.text == 'Камчатский край'
    assert browser.current_url == 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'
    element_4 =  Page.element_to_find(Locators.Spisok_partnerov)
    assert element_4.is_displayed()
    assert 'Петропавловск-Камчатский' in element_4.text
    sleep(1)
    assert browser.title == 'СБИС Контакты — Камчатский край'
