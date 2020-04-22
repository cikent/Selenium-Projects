# Import the Pytest
import pytest

# Import the Page modules created in Pages folder

""" Arrange / GIVEN Section """
# Assertion variables for each UI element on the Formy Checkbox Page that will be verified
CHECKBOX_HEADING_TEXT = 'Checkboxes'

# Define Test Function to Navigate to Formy Checkbox Page
def test_Navigate_To_Formy_Checkbox(browser):
    """ Act / WHEN Section """
    # Create an instanced Class object from the FormyCheckboxPage Class
    # Call the FormyCheckboxPage load() method and navigate to the Formy Autocomplete Page
    
    """ Assert / THEN Section """
    # Verify that the Formy Checkbox Page Heading Text matches the CHECKBOX_HEADING_TEXT variable