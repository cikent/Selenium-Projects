# Import the Pytest Library
import pytest
import json

# Import the Page modules created in Pages folder
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

# From the Selenium Webdriver Library, import the Chrome module
from selenium.webdriver import Chrome

# Create a Pytest Fixture to handle configuration parameters for the test
@pytest.fixture(scope='session')                    # Pytest decorator, scoped to each session
def config():                                       # Define the config function
    with open('test/config.json') as config_file:   # 
        data = json.load(config_file)
    return data

# Create a Pytest Fixture to handle Setup and Cleanup of Tests
@pytest.fixture                                     # Pytest decorator
def browser():                                      # Define the browser function
    driver = Chrome()                               # Initialize ChromeDriver by creating a Chrome browser object
    driver.implicitly_wait(10)                      # Set the Driver's Implicit Wait duration to 10 seconds
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

