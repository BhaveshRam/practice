import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class interactiveElements:

    def __init__(self, driver):
        self.driver = driver

    def clickLin(self, text1):
        x = self.driver.find_elements(By.TAG_NAME, "a")
        x1 = []
        for i in x:
            x1.append(i.text)
        x[x1.index(text1)].click()

    def tickCheckBoxes(self):
        x = self.driver.find_element(By.ID, "checkboxes").find_elements(By.TAG_NAME, "input")
        x[0].click()
        return x[0]

    def drpdwn(self):
        a = self.driver.find_element(By.ID, "dropdown")
        select = Select(a)
        select.select_by_visible_text("Option 1")
        return select.first_selected_option
