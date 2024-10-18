from behave import *
from pages.onboarding_pages import Onboarding_task
use_step_matcher("re")


@given("User Open the App")
def step_impl(context):
    Onboarding_task(context).open_app()



@then('User click on the "Get started" button')
def step_impl(context):
    Onboarding_task(context).click_on_get_started()


@then('User click on the "Skip" button')
def step_impl(context):
    Onboarding_task(context).skip_button()


@then('User click on the "Get started_main" button')
def step_impl(context):
    Onboarding_task(context).get_start_button()


@step('User click on the "Workspace" button')
def step_impl(context):
    Onboarding_task(context).click_workspace()


@then("User click on the profile button")
def step_impl(context):
    Onboarding_task(context).profile_button()


@step("User click on the Create new account button")
def step_impl(context):
    Onboarding_task(context).create_account_button()


@then("User Enter the valid Email and Valid Password")
def step_impl(context):
    Onboarding_task(context).valid_email_paasword()


@step("User click on the new account button")
def step_impl(context):
    Onboarding_task(context).new_account_apply_button()



@step("User click on the timeline")
def step_impl(context):
    Onboarding_task(context).click_on_timeline()


@then("User verify the account create successful")
def step_impl(context):
    Onboarding_task(context).verify_task()