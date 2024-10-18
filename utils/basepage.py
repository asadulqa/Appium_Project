from time import sleep
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction

class PageBase:
    def __init__(self,context=None,driver=None):
        if context:
            self.driver = context.driver
        else:
            self.driver = driver

    def click(self, locator):
        self.wait_for_element_to_clickable(locator)
        self.driver.find_element(*self._formatter(locator)).click()

    def wait_for_element(self,locator,timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(self._formatter(locator)))

    def wait_for_element_to_clickable(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(self._formatter(locator)))


    def scoll_screen(self):
        touch_action = TouchAction(self.driver)
        touch_action.press(x=300, y=400).wait(1000).move_to(x=500, y=700).release().perform()

    def visibility_of_element_located(self,locator, timeout = 10):
        WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(self._formatter(locator)))


    def refresh_browser(self):
        self.driver.refresh()

    def switch_to_new_window(self,win_handle):
        self.driver.switch_to.window(win_handle)


    def switch_control_to_app(self):
        '''
        Method to switch control to app
        '''
        try:
            self.driver.switch_to.context('NATIVE_APP')
        except Exception as e:
            raise Exception("Unable to switch control to app")


    def switch_control_to_webview(self):
        '''
        Method to switch control to app
        '''
        try:
            webview = self.driver.contexts[1]
            self.driver.switch_to.context(webview)
        except Exception as e:
            raise Exception(
                "Unable to switch control to webview due to " + str(e))

    def handle_pop_up(self, btn_to_click):
        """
        Method to handle (accept/reject) pop ups
        :param btn_to_click: text of the button to be clicked, e.g. "Allow", "Block"
        :return:
        """
        try:
            self.switch_control_to_app()
            self.driver.find_element_by_xpath(
                f".//*[@text='{btn_to_click}']").click()
            self.switch_control_to_webview()
        except Exception as e:
            raise Exception("Unable to handle the pop up due to " + str(e))



    def _formatter(self,locator):
        type,loc = locator.split("@@")
        if type == "id":
            return (AppiumBy.ID,loc)
        if type =="xpath":
            return (AppiumBy.XPATH,loc)


