# Import the Pytest
import pytest

# Import the Page modules created in Pages folder
from pages.Formy_Autocomplete_Page import FormyAutocompletePage

# Define Test Function to Navigate to Formy Autocomplete Page
def test_Navigate_To_Formy_Autocomplete(browser):
    """ Arrange / GIVEN Section """
    # Assertion variables for each UI element on the Formy Home Page that will be verified           
    GREETING = 'Autocomplete'                                                            

    """ Act / WHEN Section """
    # Create an instanced Class object from the FormyAutocompletePage Class
    autocomplete_page = FormyAutocompletePage(browser)
    # Call the FormyAutocompletePage load() method and navigate to the Formy Autocomplete Page
    autocomplete_page.load()
    
    """ Assert / THEN Section """
    # Verify that the Formy Autocomplete Page Heading Text matches the GREETING value
    # assert autocomplete_page.home_greeting_text == GREETING

    