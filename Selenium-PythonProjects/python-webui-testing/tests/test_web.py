"""
This module contains web test cases for the tutorial.
Tests use Selenium WebDriver with Chrome and ChromeDriver.
The fixtures set up and clean up the ChromeDriver instance.
"""

# Import the Pytest Library
import pytest

# Import the Page Objects created within the Project
from pages.search import DuckDuckGoSearchPage
# from pages.result import 

# From the Selenium Webdriver Library, import the Chrome module
from selenium.webdriver import Chrome
# From the Selenium Webdriver Common Keys Library, import the Keys module
from selenium.webdriver.common.keys import Keys

# Create a Pytest Fixture to handle Setup and Cleanup of Tests
@pytest.fixture                     # Pytest Decorator
def browser():                      # Define the function
    driver = Chrome()               # Initialize ChromeDriver by creating a Chrome browser object
    driver.implicitly_wait(10)      # Set the Driver's Implicit Wait duration to 10 seconds
    yield driver                    # Return the instanced ChromDriver object at the end of Setup
    driver.quit()                   # During Cleanup, quit/destroy the instanced ChromeDriver object

# Define Test Function to Search DuckDuckGo
def test_basic_duckduckgo_search(browser):
    """ Arrange / GIVEN Section """
    # Define Test Specifc Search Phrase                
    PHRASE = 'panda'                                                            

    search_page = DuckDuckGoSearchPage(browser)
    search_page.load
    search_page.search(PHRASE)


    """ Act / WHEN Section """
    # Find the Search Input Text Field using the Elements Id value                    
    search_input = browser.find_element_by_id('search_form_input_homepage') # The 'id' attribute = 'search_form_input_homepage' in the DOM
    # Send the Browser the Phrase then press Enter/Return
    search_input.send_keys(PHRASE + Keys.RETURN)                      

    """ Assert / THEN Section """
    # Verify that results(links) appear on the results page after the search
    link_divs = browser.find_elements_by_css_selector('#links > div')     
    assert len(link_divs) > 0                                                   

    # Verify that at least one search result contains the search phrase
    xpath = f"//div[@id='links']//*[contains(text(), '{PHRASE}')]"        
    phrase_results = browser.find_elements_by_xpath(xpath)          
    assert len(phrase_results) > 0                                                     

    # Verify that the search phrase is the same
    search_input = browser.find_element_by_id('search_form_input')
    assert search_input.get_attribute('value') == PHRASE 

