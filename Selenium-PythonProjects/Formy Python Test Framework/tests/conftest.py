# Import the Pytest & JSON Libraries
import pytest, json

# From the Selenium Webdriver Library, import the Chrome & Firefox module
from selenium.webdriver import Chrome, Firefox

# Define Configuation Variables
CONFIG_PATH = 'tests/config.json'
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome', 'firefox']

# Pytest Fixture to return JSON config file as a Dictionary object
@pytest.fixture(scope='session')
def config():
    # Read the JSON config file and returns it as a parsed dictionary
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


# Pytest Fixture to validate the config Dictionary's 'browser' Key before test execution
@pytest.fixture(scope='session')
def config_browser(config):
    # Validate and return the 'browser' value from the config data
    if 'browser' not in config:
        raise Exception('This config file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']


# Pytest Fixture to validate the config Dictionary's 'wait_time' Key before test execution
@pytest.fixture(scope='session')
def config_wait_time(config):
    # Validate and return the 'wait_time' value from the config data
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME


# Pytest Fixture to handle Setup and Cleanup of Tests
@pytest.fixture
def browser(config_browser, config_wait_time):
    # Instantiate WebDriver based upon Config data
    if config_browser == 'chrome':
        driver = Chrome()
    elif config_browser == 'firefox':
        driver = Firefox()
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')
    
    # Implicitly wait for Elements to load before interacting with them
    driver.implicitly_wait(config_wait_time)

    # Return the driver object at the end of setup
    yield driver
    
    # For Cleanup, quit/exit the driver
    driver.quit()