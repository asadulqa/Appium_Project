from behave import *
from pages.taskdetails_pages import Taskdetails
use_step_matcher("re")


@given("User open the home page")
def step_impl(context):
    Taskdetails(context).open_home_page()


@then("User click on the Board section")
def step_impl(context):
    Taskdetails(context).click_on_board()


@then("User click on the Pen icon")
def step_impl(context):
    Taskdetails(context).click_pen_icon()


@step("User Delete the project details")
def step_impl(context):
    Taskdetails(context).click_delete_button()


@then("User click on the yes delete button")
def step_impl(context):
    Taskdetails(context).click_delete()


@step("User verify the project details delete successful")
def step_impl(context):
    Taskdetails(context).verify_delete_done()