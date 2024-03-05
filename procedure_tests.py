from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

url ="https://sbis.ru/"

class Locators:
    Contacts = (By.LINK_TEXT, "Контакты")
    Tensor_link = (By.CLASS_NAME, "sbisru-Contacts__logo-tensor")
    Sila_v_lyudyah = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
    Podrobnee_link = (By.CSS_SELECTOR, '[href="/about"]')
    Rabotaem = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]')
    Region = (By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
    Spisok_partnerov = (By.XPATH, '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]')
    Kamchtskij_krai = (By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span')
    
def element_to_find(driver, locator, time=5):
    element = WebDriverWait(driver, time).until(EC.presence_of_element_located(locator))
    return element

def find_and_click(driver, locator, time=5):
    element = WebDriverWait(driver, time).until(EC.presence_of_element_located(locator))
    return element.click()

def move_to(driver, element):
    actions = ActionChains(driver)
    actions.move_to_element(element)
    return actions.perform()

def switch_windows(driver, number):
    windows = driver.window_handles
    return driver.switch_to.window(windows[number])

def test_1():
    try:
        #1
        driver = webdriver.Chrome()
        driver.maximize_window()
        sleep(2)
        driver.get(url=url)
        find_and_click(driver, Locators.Contacts)
        #2        
        find_and_click(driver, Locators.Tensor_link)
        #3
        switch_windows(driver, 1)
        assert driver.current_url == "https://tensor.ru/"
        #4
        element = element_to_find(driver, Locators.Sila_v_lyudyah)
        move_to(driver, element)
        assert element.is_displayed()
        #5
        find_and_click(driver, Locators.Podrobnee_link)
        assert driver.current_url == 'https://tensor.ru/about'
        #6
        move_to(driver, element_to_find(driver, Locators.Rabotaem))
        images = driver.find_elements(By.TAG_NAME, 'img')
        same_images_check = []
        for image in images[1:5]:
            try:
                size = image.size
                same_images_check.append((size['width'], size['height']))
            except:
                print('image could be hidden')
        assert len(set(same_images_check)) == 1
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def test_2():
    #1
    driver = webdriver.Chrome()
    driver.maximize_window()
    sleep(2)
    driver.get(url=url) 
    find_and_click(driver, Locators.Contacts)
    #2
    sleep(1)
    element_1 = element_to_find(driver, Locators.Region)
    assert element_1.text == 'Ярославская обл.'
    element_2 = element_to_find(driver, Locators.Spisok_partnerov)
    assert element_2.is_displayed()
    #3
    element_1.click()
    find_and_click(driver, Locators.Kamchtskij_krai)
    #4
    element_3 = element_to_find(driver, Locators.Region)
    sleep(1)
    assert element_3.text == 'Камчатский край'
    assert driver.current_url == 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'
    element_4 = element_to_find(driver, Locators.Spisok_partnerov)
    assert 'Петропавловск-Камчатский' in element_4.text  
    assert element_4.is_displayed()
    assert driver.title == 'СБИС Контакты — Камчатский край'
    sleep(2)
    driver.close()
    driver.quit()

test_1()
test_2()
