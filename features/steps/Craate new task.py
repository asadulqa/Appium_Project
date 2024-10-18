from behave import *
from pages.create_newtask_pages import Create_task
use_step_matcher("re")


@step('User click on the "\+" icon')
def step_impl(context):
   Create_task(context).click_plus_icon()


@then("User click on the create repeating task")
def step_impl(context):
    Create_task(context).click_repeating_button()


@step("User enter the task title")
def step_impl(context):
    Create_task(context).task_title()


@step("User enter the descriptions")
def step_impl(context):
    Create_task(context).description_title()


@then("User click on the Select project")
def step_impl(context):
    Create_task(context).select_project_button()


@step("user enter the project name and save")
def step_impl(context):
    Create_task(context).enter_project_name()

#
# @then("User click on the '\+' icon or save button")
# def step_impl(context):
#     Create_task(context).click_save_button()


@step("User click on the Set priority button")
def step_impl(context):
    Create_task(context).click_priority_button()


@then("User click on the Urgent")
def step_impl(context):
    Create_task(context).set_urgent()


@then("User click on the Add reminder button")
def step_impl(context):
    Create_task(context).click_reminder_button()


@step("User select the scheduled")
def step_impl(context):
    Create_task(context).set_reminder()


@step("User click on the Checklist button")
def step_impl(context):
    Create_task(context).click_checklist_button()


@then("User click on the Add item button")
def step_impl(context):
    Create_task(context).enter_checklist_item()


@step("User enter the checklist item name and back button")
def step_impl(context):
    Create_task(context).save_item()


@then("User click on the export button")
def step_impl(context):
    Create_task(context).export_button()


@step("User verify the Repeating task on the dashboard")
def step_impl(context):
    Create_task(context).verify_repating_task()


@then("User click on the create Note")
def step_impl(context):
    Create_task(context).click_on_create_note()


@then("User enter the Note title")
def step_impl(context):
    Create_task(context).enter_note_title()


# @then("User click on the Pin as notification button")
# def step_impl(context):
#     Create_task(context).click_pin_as_notification()


@step("User verify the Note task on the dashboard")
def step_impl(context):
    Create_task(context).verify_note_task()


@step("user click on the Note button")
def step_impl(context):
    Create_task(context).click_note_button()


@step("User verify the task on the dashboard")
def step_impl(context):
    Create_task(context).verify_task()


@given("Open the app")
def step_impl(context):
    Create_task(context).user_open_app()