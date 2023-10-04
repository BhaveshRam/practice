from selenium.webdriver.common.by import By


class AssertValid:

    def __init__(self, driver):
        self.driver = driver

    def clickbtn(self):
        x = self.driver.find_elements(By.TAG_NAME, "a")
        x1 = []
        for i in x:
            x1.append(i.text)
        x[x1.index('Add/Remove Elements')].click()

    def elementAdd(self):
        a = self.driver.find_element(By.CLASS_NAME, "example").find_element(By.XPATH,
                                                                            "//*[contains(text(),'Add Element')]")
        return a

    def deleteEl(self):
        a = self.driver.find_element(By.CLASS_NAME, "example").find_element(By.XPATH, "//*[contains(text(), 'Delete')]")
        return a
