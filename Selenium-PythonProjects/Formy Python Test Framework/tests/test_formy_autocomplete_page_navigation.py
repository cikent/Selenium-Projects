# Import the Pytest Library
import pytest

# Import the Page modules created in Pages folder
from pages.AutocompletePagePo import AutocompletePage

""" Arrange / GIVEN Section """
# Assertion variables for each UI element on the Formy Home Page that will be verified           
AUTOCOMPLETE_HEADING_TEXT = 'Autocomplete'  

# Define Test Function to Navigate to Formy Autocomplete Page
def test_Navigate_To_Formy_Autocomplete(browser):
    """ Act / WHEN Section """
    # Create an instanced Class object from the FormyAutocompletePage Class
    autocomplete_page = AutocompletePage(browser)
    # Call the FormyAutocompletePage load() method and navigate to the Formy Autocomplete Page
    autocomplete_page.load()
    
    """ Assert / THEN Section """
    # Verify that the Formy Autocomplete Page Heading Text matches the AUTOCOMPLETE_HEADING_TEXT variable
    assert autocomplete_page.autocomplete_heading_text() == AUTOCOMPLETE_HEADING_TEXT
