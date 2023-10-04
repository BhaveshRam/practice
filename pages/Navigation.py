from selenium.webdriver.common.by import By


class Navigation:
    def __init__(self, driver):
        self.driver = driver

    def clickbtn(self):
        x = self.driver.find_elements(By.TAG_NAME, "a")
        x1 = []
        for i in x:
            x1.append(i.text)
        x[x1.index('Multiple Windows')].click()

    def ret_window(self):
        self.driver.find_element(By.CLASS_NAME, "example").find_element(By.TAG_NAME, "a").click()
        self.driver.implicitly_wait(5)
        a = self.driver.window_handles
        return a

    def ret_to_default(self):
        a = self.driver.window_handles
        x = self.driver.current_window_handle
        for i in a:
            self.driver.switch_to.window(i)
            if 'Internet' in self.driver.title:
                break
            else:
                self.driver.switch_to.window(x)
