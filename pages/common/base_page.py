from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.logger import logger

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate(self, url):
        """Navigate to the specified URL."""
        logger.info(f"Navigating to URL: {url}")
        self.driver.get(url)

    def click(self, locator):
        """Click on an element identified by the locator."""
        try:
            logger.info(f"Clicking element with locator: {locator}")
            self.wait.until(EC.element_to_be_clickable(locator)).click()
        except Exception as e:
            logger.error(f"Error clicking element with locator: {locator}. Error: {e}")
            raise

    def type(self, locator, text):
        """Type text into an element identified by the locator."""
        try:
            logger.info(f"Typing text '{text}' into element with locator: {locator}")
            self.wait.until(EC.presence_of_element_located(locator)).send_keys(text)
        except Exception as e:
            logger.error(f"Error typing text '{text}' into element with locator: {locator}. Error: {e}")
            raise

    def get_text(self, locator):
        """Get text from an element identified by the locator."""
        try:
            text = self.wait.until(EC.presence_of_element_located(locator)).text
            logger.info(f"Fetched text '{text}' from element with locator: {locator}")
            return text
        except Exception as e:
            logger.error(f"Error fetching text from element with locator: {locator}. Error: {e}")
            raise














# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from utilities.logger import logger
#
# class BasePage:
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10)
#
#     def navigate(self, url):
#         """Navigate to the specified URL."""
#         logger.info(f"Navigating to URL: {url}")
#         self.driver.get(url)
#
#     def click(self, locator):
#         """Click on an element identified by the locator."""
#         logger.info("Clicking on element with locator: %s" )
#         self.wait.until(EC.element_to_be_clickable(locator)).click()
#
#     def type(self, locator, text):
#         """Type text into an element identified by the locator."""
#         self.wait.until(EC.presence_of_element_located(locator)).send_keys(text)
#
#     def get_text(self, locator):
#         """Get text from an element identified by the locator."""
#         return self.wait.until(EC.presence_of_element_located(locator)).text
#

