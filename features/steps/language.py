from behave import *
from pages.change_language_pages import Language

use_step_matcher("re")

@given("User Open app")
def step_impl(context):
    Language(context).open()


@then("User click on the Workspace")
def step_impl(context):
    Language(context).click_on_workspace()


@step("User click on the setting button")
def step_impl(context):
    Language(context).click_on_setting()


@step("User click on the Language button")
def step_impl(context):
    Language(context).click_on_language_button()


@then("User select the Language")
def step_impl(context):
    Language(context).select_language()


@step("User verify the language changed successfully")
def step_impl(context):
    Language(context).verify_change_language()


@then("User click_back_button")
def step_impl(context):
    Language(context).click_back()