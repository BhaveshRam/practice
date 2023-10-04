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

from pages.Navigation import Navigation


class Nav_test(unittest.TestCase):
    service = Service(executable_path="..\\drivers\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    def test_a(self):
        self.driver.get("https://the-internet.herokuapp.com/")
        self.driver.implicitly_wait(20)

    def test_btnCk(self):
        n = Navigation(self.driver)
        n.clickbtn()
        self.driver.implicitly_wait(5)
        x = self.driver.find_element(By.TAG_NAME, "h3")
        allure.attach(self.driver.get_screenshot_as_png(), name="linkclick", attachment_type=AttachmentType.PNG)
        assert 'new window' in x.text

    def test_openwd(self):
        n = Navigation(self.driver)
        hd = n.ret_window()
        x = self.driver.current_window_handle
        for i in hd:
            self.driver.switch_to.window(i)
            if 'New' in self.driver.title:
                break
            else:
                self.driver.switch_to.window(x)
        allure.attach(self.driver.get_screenshot_as_png(), name="NewWindow", attachment_type=AttachmentType.PNG)
        assert 'New Window' in self.driver.title

    def test_zdefWindow(self):
        n = Navigation(self.driver)
        n.ret_to_default()
        allure.attach(self.driver.get_screenshot_as_png(), name="Defwindow", attachment_type=AttachmentType.PNG)
        assert "The Internet" in self.driver.title
