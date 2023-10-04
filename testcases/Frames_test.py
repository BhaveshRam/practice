from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import sys
import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

sys.path.append("C:/Users/Bhavesh_ram/PycharmProjects/LearningTrack")

from pages.Frames import Frames


class Frames_test(unittest.TestCase):
    service = Service('../drivers/chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    def test_1(self):
        self.driver.get("https://the-internet.herokuapp.com/")
        self.driver.implicitly_wait(10)

    def test_2_Click(self):
        fm = Frames(self.driver)
        fm.clickButton()

        a = self.driver.find_element(By.TAG_NAME, "h3")
        allure.attach(self.driver.get_screenshot_as_png(), name="FramesPage", attachment_type=AttachmentType.PNG)
        assert "Frames" in a.text

    def test_3_nested(self):
        fm = Frames(self.driver)

        a = fm.Nested_frame()
        a.click()
        x = self.driver.find_elements(By.TAG_NAME, "frame")
        allure.attach(self.driver.get_screenshot_as_png(), name="NestedFrame", attachment_type=AttachmentType.PNG)
        assert len(x) == 2

    def test_4_nested_top(self):
        fm = Frames(self.driver)

        a = fm.Nested_frame_top()
        self.driver.switch_to.frame(a)

        x = self.driver.find_elements(By.TAG_NAME, "frameset")

        assert len(x) == 1

    def test_5_nested_left(self):
        fm = Frames(self.driver)

        a = fm.Nested_frame_left()
        self.driver.switch_to.frame(a)

        x = self.driver.find_element(By.TAG_NAME, "body")

        assert "LEFT" in x.text

    def test_6_iframe(self):
        fm = Frames(self.driver)
        self.driver.back()

        x = self.driver.find_element(By.TAG_NAME, "h3")
        if 'Frames' in x.text:
            a = fm.iFrame()
            a.click()
            x = self.driver.find_element(By.TAG_NAME, "h3")
            assert 'iFrame' in x.text
        else:
            assert False

    def test_7_iframe(self):
        fm = Frames(self.driver)

        a = fm.shift_iframe()
        self.driver.switch_to.frame(a)

        x = self.driver.find_element(By.TAG_NAME, "body").find_element(By.TAG_NAME, "p")
        x.send_keys("ram")
        allure.attach(self.driver.get_screenshot_as_png(), name="iFrameText", attachment_type=AttachmentType.PNG)
        assert "ram" in x.text
