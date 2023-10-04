from selenium.webdriver.common.by import By


class Frames:
    def __init__(self, driver):
        self.driver = driver

    def clickButton(self):
        x = self.driver.find_elements(By.TAG_NAME, "a")
        x1 = []
        for i in x:
            x1.append(i.text)
        x[x1.index('Frames')].click()

    def Nested_frame(self):
        a = self.driver.find_element(By.CLASS_NAME, "example").find_element(By.XPATH, "//*[contains(text(), 'Nested "
                                                                                      "Frames')]")
        return a

    def iFrame(self):
        a = self.driver.find_element(By.CLASS_NAME, "example").find_element(By.XPATH, "//*[contains(text(), 'iFrame')]")
        return a

    def Nested_frame_top(self):
        a = self.driver.find_element(By.NAME, "frame-top")
        return a

    def Nested_frame_middle(self):
        a = self.driver.find_element(By.NAME, "frame-middle")
        return a

    def Nested_frame_bottom(self):
        a = self.driver.find_element(By.NAME, "frame-bottom")
        return a

    def Nested_frame_left(self):
        a = self.driver.find_element(By.NAME, "frame-left")
        return a

    def Nested_frame_right(self):
        a = self.driver.find_element(By.NAME, "frame-right")
        return a

    def shift_iframe(self):
        a = self.driver.find_element(By.TAG_NAME, "iframe")
        return a
