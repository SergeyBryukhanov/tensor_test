from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from BasePage import BasePage

class Locators:
    Contacts = (By.LINK_TEXT, "Контакты")
    Tensor_link = (By.CLASS_NAME, "sbisru-Contacts__logo-tensor")
    Sila_v_lyudyah = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
    Podrobnee_link = (By.CSS_SELECTOR, '[href="/about"]')
    Rabotaem = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[2]')
    Region = (By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
    Spisok_partnerov = (By.XPATH, '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]')
    Kamchtskij_krai = (By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span/span')


class PageObject(BasePage):
    
    def element_to_find(self, locator, time=5):
        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
        return element

    def find_and_click(self, locator, time=5):
        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))
        return element.click()
    
    def move_to(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        return actions.perform()

    def switch_windows(self, number):
        windows = self.driver.window_handles
        return self.driver.switch_to.window(windows[number])
    
    def find_images(self):
        return self.driver.find_elements(self, By.TAG_NAME, 'img')
        