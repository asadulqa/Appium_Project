from pages.base_page import BaseDriver
from locators import app_locator

class Taskdetails(BaseDriver):
    def open_home_page(self):
        pass

    def click_on_board(self):
        self.click(app_locator.board_button)

    def click_pen_icon(self):
        self.wait_for_element(app_locator.pen_icon)
        self.click(app_locator.pen_icon)

    def click_delete_button(self):
        self.wait_for_element(app_locator.delete_button)
        self.click(app_locator.delete_button)

    def click_delete(self):
        self.wait_for_element(app_locator.delete_sure_button)
        self.click(app_locator.delete_sure_button)


    def verify_delete_done(self):
        self.wait_for_element(app_locator.create_project)
        project_name = self.driver.find_element(*self. _formatter(app_locator.create_project)).text
        print(project_name)
        assert project_name == "Create project"