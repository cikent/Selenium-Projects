# Import the Pytest & JSON Libraries
import pytest, json

# From the Selenium Webdriver Library, import the Chrome module
from selenium.webdriver import Chrome, Firefox

# Import the Page modules created in Pages folder
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

# Create a Pytest Fixture to handle configuration parameters for the test
@pytest.fixture(scope='session')                    # Pytest decorator, scoped to execute once each test session
def config():                                       # Function to load config data
    with open('tests/config.json') as config_file:   # Open the JSON config file
        data = json.load(config_file)               # Store the contents of the file
    return data                                     # Return the variable holding the config data


# Create a Pytest Fixture to handle Setup and Cleanup of Tests
@pytest.fixture                                     # Pytest decorator
def browser(config):                                # Define the browser function and pass config() data to it
    if config['browser'] == 'chrome':               # Check to see if config matches Chrome
        driver = Chrome()                           # Initialize ChromeDriver by creating a Chrome browser object
    elif config['browser'] == 'firefox':            # Check to see if config matches Firefox
        driver = Firefox()                          # Initialize GeckoDriver by creating a Firefox browser object
    else:                                           # Otherwise, raise Exception and prompt User about error
        raise Exception(f'"{config["browser"]}" is not a supported browser')
   
    driver.implicitly_wait(config['wait_time'])     # Set the Driver's Implicit Wait duration based upon the 'wait_time' config value
    yield driver                                    # Return the instanced ChromDriver object at the end of Setup
    driver.quit()                                   # During Cleanup, quit/destroy the instanced ChromeDriver object


# Define Test Function to Search DuckDuckGo
def test_basic_duckduckgo_search(browser):
    """ Arrange / GIVEN Section """
    # Define a test specifc search phrase (i.e. Set up test case data)               
    PHRASE = 'panda'                                                            

    """ Act / WHEN Section """
    # Create an instanced Class object from the DuckDuckGoSearchPage Class
    search_page = DuckDuckGoSearchPage(browser)
    # Call the DuckDuckGoSearchPage Load method and navigate to the Duck Duck Go home page
    search_page.load()
    # Find the Search Text field and pass in the Search
    search_page.search(PHRASE)

    """ Assert / THEN Section """
    # Create an instanced Class object from the DuckDuckGoResultsPage Class
    results_page = DuckDuckGoResultPage(browser)
    # Verify the 'div' called Links returns more than zero links
    assert results_page.link_div_count() > 0
    # Verify the 'div' called Links returns more than zero links that match the search phrase value
    assert results_page.phrase_result_count(PHRASE) > 0
    # Verify that the Results page Search Text Field value matches the search phrase
    assert results_page.search_input_value() == PHRASE

