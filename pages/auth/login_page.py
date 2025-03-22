from selenium.webdriver.common.by import By
from pages.common.base_page import BasePage

class LoginPage(BasePage):
    # Locators for login page elements
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "orangehrm-login-button")
    DASHBOARD_ELEMENT = (By.CLASS_NAME, "oxd-main-menu-item--name")

    def enter_credentials(self, username, password):
        """Enter username and password, then click login."""
        self.type(self.USERNAME_FIELD, username)
        self.type(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    #optional method
    # def is_dashboard_displayed(self):
    #     """Check if the dashboard element is displayed."""
    #     dashboard_element = self.driver.find_element(*self.DASHBOARD_ELEMENT)
    #     return dashboard_element.is_displayed() and dashboard_element.text == "Dashboard"
