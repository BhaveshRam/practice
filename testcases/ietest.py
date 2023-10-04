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

from pages.interactiveElements import interactiveElements


class ietest(unittest.TestCase):
    service = Service(executable_path="..\\drivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    @allure.severity(allure.severity_level.BLOCKER)
    def test_ainPage(self):
        self.driver.get("https://the-internet.herokuapp.com/")
        WebDriverWait(self.driver,20).until(EC.text_to_be_present_in_element((By.TAG_NAME,"h1"),"Welcome to the-internet"))

    # def test_print(self):
    #     ie = interactiveElements(self.driver)
    #     ie.printDriv()

    def test_checkBoxes(self):
        self.driver.get("https://the-internet.herokuapp.com/")
        self.driver.implicitly_wait(10)
        ie = interactiveElements(self.driver)
        ie.clickLin('Checkboxes')
        self.driver.implicitly_wait(10)
        a = ie.tickCheckBoxes()
        allure.attach(self.driver.get_screenshot_as_png(), name="CheckBoxes", attachment_type=AttachmentType.PNG)
        assert a.is_selected()

    def test_dropdown(self):
        self.driver.get("https://the-internet.herokuapp.com/")
        self.driver.implicitly_wait(10)
        ie = interactiveElements(self.driver)
        ie.clickLin("Dropdown")
        self.driver.implicitly_wait(10)
        a = ie.drpdwn()
        allure.attach(self.driver.get_screenshot_as_png(), name="drpdown", attachment_type=AttachmentType.PNG)
        assert a.text == 'Option 1'

