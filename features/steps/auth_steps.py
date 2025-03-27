from allure_commons._allure import attach
from behave import given, when, then
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv
from pages.auth.login_page import LoginPage
from utilities.browser_manager import get_driver
from utilities.logger import logger

load_dotenv(dotenv_path=".env")


@given("the user is on the login page")
def step_impl(context):
    # Initialize WebDriver and navigate to the login page
    context.driver = get_driver()
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@when("the user enters valid credentials")
def step_impl(context):
    username = os.getenv("LOGIN_USERNAME")
    password = os.getenv("LOGIN_PASSWORD")
    logger.info("Entering credentials: username=%s", username)
    context.login_page.enter_credentials(username, password)
    logger.info("Successfully entered credentials.")
    time.sleep(3)


@then("the user should be redirected to the dashboard")
def step_impl(context):
    try:
        dashboard_element = context.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']")
        assert dashboard_element.is_displayed(), "Dashboard element not found."
        logger.info("Dashboard is displayed successfully.")
    except Exception as e:
        logger.error("Error verifying dashboard: %s", str(e))
        raise
    finally:
        context.driver.quit()
        logger.info("Browser session ended.")
    # attach(context.driver.get_screenshot_as_png(), name="Dashboard Screenshot", attachment_type="image/png")

@when("the user enters a valid username and an incorrect password")
def step_user_enters_invalid_password(context):
    for row in context.table:
        context.login_page.enter_credentials(row["Username"], row["Password"])
    time.sleep(3)
    logger.info("Entered invalid credentials")


@when("the user clicks the login button")
def step_click_login_button(context):
    context.login_page.click_login()
    logger.info("Clicked login button")

@then("the user should see an error message \"Invalid credentials\"")
def step_verify_error_message(context):
    try:
        error_message = context.login_page.get_error_message()
        assert "Invalid credendfdftials" in error_message, "Error message not found!"
        logger.info("Error message displayed correctly")
    except Exception as e:
        logger.error("Error verifying message: %s", str(e))
        raise
    finally:
        context.driver.quit()
        logger.info("Browser session ended.")





#optional for minimal logging
# @when("the user enters valid credentials")
# def step_impl(context):
#     logger.info("Entering valid credentials for the login scenario.")
#     context.login_page.enter_credentials(os.getenv("LOGIN_USERNAME"), os.getenv("LOGIN_PASSWORD"))
#
# @then("the user should be redirected to the dashboard")
# def step_impl(context):
#     logger.info("Verifying user is redirected to the dashboard.")
#     dashboard_element = context.driver.find_element(By.XPATH, "//h6[normalize-space()='Dashboard']")
#     assert dashboard_element.is_displayed(), "Dashboard element not found."
#     logger.info("Successfully verified the user is on the dashboard.")