from pages.base_page import BaseDriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import random
from locators import app_locator

class Create_task(BaseDriver):

    def user_open_app(self):

        pass

    def click_plus_icon(self):
        self.click(app_locator.plus_icon)

    def click_repeating_button(self):
        self.click(app_locator.repating_taks)

    def task_title(self):
        self.wait_for_element(app_locator.task_title,10)
        # self.click(app_locator.touch_screen)
        task_title = self.driver.find_element(*self. _formatter(app_locator.task_title))
        task_title.send_keys("It Information")

    def description_title(self):
        self.wait_for_element(app_locator.details_button)
        description = self.driver.find_element(*self. _formatter(app_locator.details_button))
        description.send_keys("Information technology (IT) is a set of related fields that encompass computer systems, software, programming languages")

    def select_project_button(self):
        self.click(app_locator.select_project)

    def enter_project_name(self):
        try:
            self.wait_for_element(app_locator.input_project_name)
            enter_project_name = self.driver.find_element(*self. _formatter(app_locator.input_project_name))
            enter_project_name.send_keys("Technology")
            self.click(app_locator.save_button)
        except:
            self.wait_for_element(app_locator.previous_project)
            self.click(app_locator.previous_project)


    # def click_save_button(self):
    #     self.click(app_locator.save_button)

    def click_priority_button(self):
        self.click(app_locator.set_priority)

    def set_urgent(self):
        self.wait_for_element(app_locator.select_priority)
        self.click(app_locator.select_priority)

    def click_reminder_button(self):
        self.wait_for_element(app_locator.add_reminder_button)
        try:
            self.click(app_locator.reminder_remove)
            self.wait_for_element(app_locator.add_reminder_button)
            self.click(app_locator.add_reminder_button)
        except:
            self.click(app_locator.add_reminder_button)

    def set_reminder(self):
        self.wait_for_element(app_locator.select_reminder,10)
        self.click(app_locator.select_reminder)
        self.click(app_locator.selet_data)
        self.wait_for_element(app_locator.ok_button)
        self.click(app_locator.ok_button)

    def click_checklist_button(self):
        self.click(app_locator.add_checklist)

    def enter_checklist_item(self):
        self.wait_for_element(app_locator.checklist_titile_name,10)
        enter_item = self.driver.find_element(*self. _formatter(app_locator.checklist_titile_name))
        enter_item.send_keys("Ak IT.inc")


    def save_item(self):
        self.click(app_locator.save_button)
        self.wait_for_element(app_locator.touch_screen)
        self.click(app_locator.touch_screen)

    def export_button(self):
        self.click(app_locator.done_button)

    def verify_repating_task(self):
        self.wait_for_element(app_locator.timeline_button)
        timeline = self.driver.find_element(*self._formatter(app_locator.taskito)).text
        assert timeline == "Taskito"
        print("Account Create Done")


    def click_on_create_note(self):
        self.click(app_locator.note_button)

    def enter_note_title(self):
        self.wait_for_element(app_locator.task_title)
        note_title = self.driver.find_element(*self. _formatter(app_locator.task_title))
        note_title.send_keys("AiInformation")

    def click_pin_as_notification(self):
        self.scroll_down()
        self.click(app_locator.pin_button)


    def verify_note_task(self):
        self.wait_for_element(app_locator.taskito,10)
        taskitos = self.driver.find_element(*self. _formatter(app_locator.taskito)).text
        print("Verify that Note task done")
        assert taskitos == "Taskito"


    def click_note_button(self):
        self.click(app_locator.task_button)


    def verify_task(self):
        self.wait_for_element(app_locator.taskito)
        taskito = self.driver.find_element(*self. _formatter(app_locator.taskito)).text
        assert taskito == "Taskito"
        print("Verify that repating task done")






