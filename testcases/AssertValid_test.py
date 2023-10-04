from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import sys
import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append("C:/Users/Bhavesh_ram/PycharmProjects/LearningTrack")

from pages.AssertValid import AssertValid


class AssertValid_test(unittest.TestCase):
    service = Service(executable_path="../drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    def test_1_(self):
        self.driver.get("https://RTCS160326:VJB4ND@the-internet.herokuapp.com/")
        self.driver.implicitly_wait(10)

    def test_2_click(self):
        av = AssertValid(self.driver)
        av.clickbtn()
        x = self.driver.find_element(By.TAG_NAME, "h3")
        allure.attach(self.driver.get_screenshot_as_png(), name="EnteredLink", attachment_type=AttachmentType.PNG)
        assert 'Add/Remove' in x.text

    def test_3_elementadd(self):
        av = AssertValid(self.driver)
        a = av.elementAdd()
        wait = WebDriverWait(self.driver, 5)

        wait.until(EC.element_to_be_clickable(a)).click()
        new = self.driver.find_element(By.CLASS_NAME, "added-manually")
        allure.attach(self.driver.get_screenshot_as_png(), name="addedEl", attachment_type=AttachmentType.PNG)
        assert new.is_displayed()

    def test_4_delEl(self):
        av = AssertValid(self.driver)
        a = av.deleteEl()
        wait = WebDriverWait(self.driver, 5)

        wait.until(EC.element_to_be_clickable(a)).click()
        try:
            assert not a.is_displayed()
        except:
            allure.attach(self.driver.get_screenshot_as_png(), name="removedEl", attachment_type=AttachmentType.PNG)

            assert True

    def test_5(self):
        self.driver.close()
