from selenium import webdriver

def get_driver(browser="chrome"):
    """
    Get the WebDriver instance for the specified browser.
    Supported browsers: chrome, firefox.
    """
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.maximize_window()
    return driver
