# Import the Pytest Library
import pytest

# Import the Page modules created in Pages folder
from pages.Formy_Checkbox_Page import FormyCheckboxPage

""" Arrange / GIVEN Section """
# Assertion variables for each UI element on the Formy Checkbox Page that will be verified
CHECKBOX_HEADING_TEXT = 'Checkboxes'

# Define Test Function to Navigate to Formy Checkbox Page
def test_Navigate_To_Formy_Checkbox(browser):
    """ Act / WHEN Section """
    # Create an instanced Class object from the FormyCheckboxPage Class
    checkbox_page = FormyCheckboxPage(browser)
    # Call the FormyCheckboxPage load() method and navigate to the Formy Checkbox Page
    checkbox_page.load()
    
    """ Assert / THEN Section """
    # Verify that the Formy Checkbox Page Heading Text matches the CHECKBOX_HEADING_TEXT variable
    assert checkbox_page.checkbox_heading_text() == CHECKBOX_HEADING_TEXT
    