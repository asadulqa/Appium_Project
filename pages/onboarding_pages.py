from pages.base_page import BaseDriver
from time import sleep
from selenium.webdriver.common.by import By
import random
from locators import app_locator

class Onboarding_task(BaseDriver):

    def open_app(self):

        pass

    def click_on_get_started(self):
        self.click(app_locator.get_started_button)


    def skip_button(self):
        self.wait_for_element(app_locator.skip_button)
        self.click(app_locator.skip_button)

    def get_start_button(self):
        self.click(app_locator.get_started)

    def click_workspace(self):
        self.wait_for_element(app_locator.workspace_button)
        self.click(app_locator.workspace_button)

    def profile_button(self):
        self.wait_for_element(app_locator.profile_button)
        self.click(app_locator.profile_button)


    def create_account_button(self):
        self.wait_for_element(app_locator.create_account)
        self.click(app_locator.create_account)

    def valid_email_paasword(self):
        self.wait_for_element(app_locator.enter_mail)
        enter_mail = self.driver.find_element(*self._formatter(app_locator.enter_mail))
        emils = random.randint(1,1000000)
        enter_mail.send_keys(f"mdasdul{emils}@gmail.com")
        self.wait_for_element_to_clickable(app_locator.enter_password)
        enter_password = self.driver.find_element(*self. _formatter(app_locator.enter_password))
        enter_password.send_keys("12345678")


    def new_account_apply_button(self):
        self.wait_for_element_to_clickable(app_locator.new_account,10)
        self.click(app_locator.new_account)
        sleep(10)


    def click_on_timeline(self):
        self.wait_for_element(app_locator.timeline_button)
        self.click(app_locator.timeline_button)

    def verify_task(self):
        self.wait_for_element(app_locator.timeline_button)
        timeline = self.driver.find_element(*self. _formatter(app_locator.taskito)).text
        assert timeline == "Taskito"
        print("Account Create Done")

