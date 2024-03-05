class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        
    def open_sbis(self):
        return self.driver.get("https://sbis.ru/")
   
    def switch_windows(self, number):
        windows = self.driver.window_handles
        return self.driver.switch_to.window(windows[number])