from PageObject import Locators
from PageObject import PageObject
from time import sleep

def test_case_1(browser):
    #1
    Page = PageObject(browser)
    Page.open_sbis()
    sleep(2)
    Page.find_and_click(Locators.Contacts)
    #2
    Page.find_and_click(Locators.Tensor_link)
    #3
    Page.switch_windows(1)
    assert browser.current_url == "https://tensor.ru/"
    #4
    element = Page.element_to_find(Locators.Sila_v_lyudyah)
    Page.move_to(element)
    assert element.is_displayed()
    #5
    Page.find_and_click(Locators.Podrobnee_link)
    assert browser.current_url == 'https://tensor.ru/about'
    #6
    Page.move_to(Page.element_to_find(Locators.Rabotaem))
    images = Page.find_images()
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
    Page = PageObject(browser)
    Page.open_sbis()
    sleep(2)
    Page.find_and_click(Locators.Contacts)
    #2
    element_1 = Page.element_to_find(Locators.Region)
    assert element_1 == 'Ярославская обл.'
    element_2 = Page.element_to_find(Locators.Spisok_partnerov)
    assert element_2.is_displayed()
    #3
    element_1.click()
    Page.find_and_click(Locators.Kamchtskij_krai)
    sleep(1)
    #4
    element_1 = Page.element_to_find(Locators.Region)
    assert element_1 == 'Камчатский край'
    assert browser.current_url == 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'
    element_3 =  Page.element_to_find(Locators.Kamchatka_partner)
    assert element_3.is_displayed()
    sleep(1)
    assert browser.title == 'СБИС Контакты — Камчатский край'
    