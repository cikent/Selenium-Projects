# Import the Pytest Library
import pytest

# Import the Page modules created in Pages folder
from pages.CompleteWebFormPagePo import CompleteWebFormPage

""" Arrange / GIVEN Section """
# Assertion variables for each UI element on the Web Form Page that will be verified
COMPLETE_WEB_FORM_HEADING_TEXT = 'Complete Web Form'

# Define Test Function to Navigate to Web Form Page
def test_Navigate_To_Formy_Web_Form(browser):
    """ Act / WHEN Section """
    # Create an instanced Class object from the Web Form Page Class
    complete_web_form_page = CompleteWebFormPage(browser)

    # Call the Web Form Page load() method and navigate to the Web Form Page
    complete_web_form_page.load()

    """ Assert / THEN Section """
    # Verify that the Web Form Page Heading Text matches the WEB_FORM_HEADING_TEXT variable
    assert complete_web_form_page.complete_web_form_heading_text() == COMPLETE_WEB_FORM_HEADING_TEXT
