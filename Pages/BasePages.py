from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

'''This class is parent of all class
This class contains all the generic methods and utilities for all pages
'''


class BasePages:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_key(self,by_locator,text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)
    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title