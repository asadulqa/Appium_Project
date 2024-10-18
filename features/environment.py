# from selenium import webdriver
from appium import webdriver
from time import sleep
# from webdriver_manager.chrome import ChromeDriverManager

desired_caps = {

    "platformName": "Android",
    "platformVersion": "13",
    "deviceName": "Redmi Note 11",
    "appPackage": "com.fenchtose.reflog",
    "appActivity": "com.fenchtose.reflog.MainActivity",
    "automationName": "UiAutomator2",
    "noReset": "true"
}

def before_scenario(context, scenario):
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    sleep(3)

def after_scenario(context, scenario):
    context.driver.quit()

