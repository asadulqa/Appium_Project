from pages.base_page import BaseDriver
from time import sleep
from selenium.webdriver.common.by import By
import random
from appium.webdriver.common.touch_action import TouchAction

from locators import app_locator

class Language(BaseDriver):

    def open(self):
        pass

    def click_on_workspace(self):
        self.wait_for_element(app_locator.workspace_button)
        self.click(app_locator.workspace_button)

    def click_on_setting(self):
        self.wait_for_element(app_locator.setting_button)
        self.click(app_locator.setting_button)

    def click_on_language_button(self):
        self.wait_for_element(app_locator.language_button)
        self.click(app_locator.language_button)

    def select_language(self):
        self.wait_for_element(app_locator.english_language)
        self.click(app_locator.english_language)

    def click_on_back(self):
        self.wait_for_element(app_locator.back_button)
        self.click(app_locator.back_button)


    def verify_change_language(self):
        self.wait_for_element(app_locator.workspace_title)
        setting_title = self.driver.find_element(*self._formatter(app_locator.workspace_title))
        print(setting_title)
        assert setting_title == "Workspace"
        print("Language has changed")