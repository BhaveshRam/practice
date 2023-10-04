from selenium.webdriver.common.by import By


class alertsAndpopups:

    def __init__(self, driver):
        self.driver = driver

    def clickbtn(self):
        x = self.driver.find_elements(By.TAG_NAME, "a")
        x1 = []
        for i in x:
            x1.append(i.text)
        x[x1.index('JavaScript Alerts')].click()

    def alertClick(self):
        x = self.driver.find_element(By.CLASS_NAME, "example").find_element(By.XPATH, "//*[contains(text(), 'Click for "
                                                                                      "JS Alert')]")
        return x

    def confirmClick(self):
        x = self.driver.find_element(By.CLASS_NAME, "example").find_element(By.XPATH, "//*[contains(text(), 'Click for "
                                                                                      "JS Confirm')]")
        return x

    def promptClick(self):
        x = self.driver.find_element(By.CLASS_NAME, "example").find_element(By.XPATH, "//*[contains(text(), 'Click for "
                                                                                      "JS Prompt')]")
        return x
