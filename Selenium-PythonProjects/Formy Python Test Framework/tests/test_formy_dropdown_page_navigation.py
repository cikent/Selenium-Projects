# Import the Pytest Library
import pytest

# Import the modules created in the Pages folder
from pages.DropdownPagePo import DropdownPage

""" Arrange / GIVEN Section """
# Assertion variables for each UI element on the Formy Dropdown Page that will be verified
DROPDOWN_HEADING_TEXT = 'Dropdown'

# Define Test Function to Navigate to Formy Dropdown Page
def test_Navigate_To_Formy_Dropdown(browser):
    """ Act / WHEN Section """
    # Create an instanced Class object from the FormyDropdownPage Class
    dropdown_page = DropdownPage(browser)
    # Call the FormyDropdownPage load() method and navigate to the Formy Dropdown Page
    dropdown_page.load()
    
    """ Assert / THEN Section """
    # Verify that the Formy Dropdown Page Heading Text matches the DROPDOWN_HEADING_TEXT variable
    assert dropdown_page.dropdown_heading_text() == DROPDOWN_HEADING_TEXT
