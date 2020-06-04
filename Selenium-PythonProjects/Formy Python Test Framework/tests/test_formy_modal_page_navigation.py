# Import the Pytest Library
import pytest

# Import the Page modules created in Pages folder
from pages.Formy_Modal_Page import FormyModalPage

""" Arrange / GIVEN Section """
# Assertion variables for each UI element on the Modal Page that will be verified
MODAL_HEADING_TEXT = 'Modal'

# Define Test Function to Navigate to Modal Page
def test_Navigate_To_Formy_Modal(browser):
    """ Act / WHEN Section """
    # Create an instanced Class object from the Modal Page Class
    modal_page = FormyModalPage(browser)

    # Call the Modal Page load() method and navigate to the Modal Page
    modal_page.load()

    """ Assert / THEN Section """
    # Verify that the Modal Page Heading Text matches the MODAL_HEADING_TEXT variable
    assert modal_page.modal_heading_text() == MODAL_HEADING_TEXT
