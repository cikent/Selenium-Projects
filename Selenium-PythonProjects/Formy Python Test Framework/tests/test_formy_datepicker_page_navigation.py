# Import the Pytest Library
import pytest

# Import the Page modules created in Pages folder
from pages.Formy_Datepicker_Page import FormyDatepickerPage

""" Arrange / GIVEN Section """
# Assertion variables for each UI element on the Formy Datepicker Page that will be verified
DATEPICKER_HEADING_TEXT = "Datepicker"

# Define Test Function to Navigate to Formy Datepicker Page
def test_Navigate_To_Formy_Datepicker(browser):
    """ Act / WHEN Section """
    # Create an instanced Class object from the FormyDatepickerPage Class
    datepicker_page = FormyDatepickerPage(browser)
    # Call the FormyDatepickerPage load() method and navigate to the Formy Datepicker Page
    datepicker_page.load()
    
    """ Assert / THEN Section """
    # Verify that the Formy Datepicker Page Heading Text matches the DATEPICKER_HEADING_TEXT variable
    assert datepicker_page.datepicker_heading_text() == DATEPICKER_HEADING_TEXT
