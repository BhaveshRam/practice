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

from pages.alertsAndpopups import alertsAndpopups


class alertsPopups_test(unittest.TestCase):
    service = Service(executable_path='../drivers/chromedriver.exe')
    driver = webdriver.Chrome(service=service)

    def test_1(self):
        self.driver.get("https://the-internet.herokuapp.com/")
        self.driver.implicitly_wait(10)

    def test_2_clickbtn(self):
        ap = alertsAndpopups(self.driver)
        ap.clickbtn()

        x = self.driver.find_element(By.TAG_NAME, "h3")
        assert 'Alerts' in x.text

    def test_3_AlertDisplay(self):
        self.driver.implicitly_wait(5)
        ap = alertsAndpopups(self.driver)
        a = ap.alertClick()
        a.click()
        # allure.attach(self.driver.get_screenshot_as_png(), name="alertDisplay", attachment_type=AttachmentType.PNG)
        # return True

    def test_4_AlertClick(self):
        self.driver.implicitly_wait(5)
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

        a = self.driver.find_element(By.ID, "result")
        allure.attach(self.driver.get_screenshot_as_png(), name="Alert accepted", attachment_type=AttachmentType.PNG)
        assert "successfully" in a.text

    def test_5_AlertConfirm(self):
        self.driver.implicitly_wait(5)
        ap = alertsAndpopups(self.driver)
        a = ap.confirmClick()
        a.click()

    def test_6_AlertConfirmClick(self):
        self.driver.implicitly_wait(5)
        wait = WebDriverWait(self.driver, 10)

        wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.dismiss()

        a = self.driver.find_element(By.ID, "result")
        allure.attach(self.driver.get_screenshot_as_png(), name="alertDismissed", attachment_type=AttachmentType.PNG)
        assert "clicked" in a.text

    def test_7_AlertPrompt(self):
        ap = alertsAndpopups(self.driver)
        a = ap.promptClick()
        a.click()

    def test_8_AlertPromptClick(self):
        self.driver.implicitly_wait(5)

        alert = self.driver.switch_to.alert
        alert.send_keys("Hello Ram")
        alert.accept()

        a = self.driver.find_element(By.ID, "result")
        allure.attach(self.driver.get_screenshot_as_png(), name="promptEntered", attachment_type=AttachmentType.PNG)
        assert "Hello Ram" in a.text

