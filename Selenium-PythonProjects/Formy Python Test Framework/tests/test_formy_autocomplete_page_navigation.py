# Import the Pytest
import pytest

# Import the Page modules created in Pages folder
from pages.Formy_Autocomplete_Page import FormyAutocompletePage

# Define Test Function to Search DuckDuckGo
def test_navigate_to_Autocomplete(browser):
    """ Arrange / GIVEN Section """
    # Assertion variables for each UI element on the Formy Home Page that will be verified           
    GREETING = 'Autocomplete'                                                            

    """ Act / WHEN Section """
    # Create an instanced Class object from the Formy Class
    home_page = FormyAutocompletePage(browser)
    # Call the FormyHomePage load() method and navigate to the Formy Home Page
    home_page.load()
    
    """ Assert / THEN Section """
    # Verify that the Formy Home Page Heading Text matches the GREETING text
    # assert home_page.home_greeting_text == GREETING
    