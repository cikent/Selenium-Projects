# Import the Pytest Library
import pytest

# From the Selenium Webdriver Library, import the Chrome module
from selenium.webdriver import Chrome
# From the Selenium Webdriver Common Keys Library, import the Keys module
from selenium.webdriver.common.keys import keys

# Create a Pytest Fixture to handle Setup and Cleanup of Tests
@pytest.fixture                     # Pytest Decorator
def browser():                      # Define the function
    driver = Chrome()               # Create a Chrome browser Object
    driver.implicitly_wait(10)      # Set the Driver's Implicit Wait duration to 10 seconds
    yield driver                    # 
    driver.quit()


"""
Test Procedure:
1. Navigate to the DuckDuckGo home page
2. Enter the Search Phase
3. Verify that:
    a. Results appear on the results page
    b. The search phrase appears in the search bar
    c. At least one search result contains the search phrase
"""

# Define Test Function to Search DuckDuckGo
def test_basic_duckduckgo_search(browser):
    # Define Test Variables                 # Arrange / GIVEN
    URL = 'https://www.duckduckgo.com'
    PHRASE = 'panda'

    # Navigate to the URL utilizing the instantiated Browser
    browser.get(URL)                        # Act / WHEN

    # Find the Search Text Field using the Elements Id value
    search_input = browser.find_element_by_id('search_form_input_homepage')     # Assert / THEN
    # Send the Browser the Phrase then press Enter/Return
    search_input.send_keys(PHRASE + Keys.RETURN)
