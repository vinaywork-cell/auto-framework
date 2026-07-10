from behave import given, when, then
from pages.login_click_myteam_page import LoginPage
import os
from dotenv import load_dotenv

load_dotenv()

TARGET_URL = os.getenv("TARGET_URL")
USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")

load_dotenv()
env = os.getenv('ENV', 'dev')  # Default to 'dev' if ENV is not set

@given('I am on the login page')
def step_impl(context):
    context.page.goto(TARGET_URL)

@when('I enter valid credentials')
def step_impl(context):
    login_page = LoginPage(context.page)
    login_page.enter_email(USER_NAME)
    login_page.enter_password(PASSWORD)

@when('I enter invalid credentials')
def step_impl(context):
    login_page = LoginPage(context.page)
    login_page.enter_email('invalid@example.com')
    login_page.enter_password('invalidpassword')

@when('I click the login button')
def step_impl(context):
    login_page = LoginPage(context.page)
    login_page.click_login()

@then('I should be redirected to the dashboard')
def step_impl(context):
    context.page.wait_for_url('**/dashboard')
    assert '/dashboard' in context.page.url, f"Expected dashboard page but got {context.page.url}"

@then('I navigate to MyTeam')
def step_impl(context):
    login_page = LoginPage(context.page)
    login_page.click_myteam()
    assert 'https://utrack-beta.undocked-product.app/pages/myteam' in context.page.url, f"Expected MyTeam page but got {context.page.url}"

@then('I should see an error message')
def step_impl(context):
    assert context.page.get_by_role('alert').is_visible(), "Error message not visible"