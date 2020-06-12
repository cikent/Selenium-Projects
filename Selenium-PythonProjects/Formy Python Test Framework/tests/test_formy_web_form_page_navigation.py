# Import the Pytest Library
import pytest

# Import the Page modules created in Pages folder
from pages.Formy_Web_Form_Page import FormyWebFormPage

""" Arrange / GIVEN Section """
# Assertion variables for each UI element on the Web Form Page that will be verified
WEB_FORM_HEADING_TEXT = 'Complete Web Form'

# Define Test Function to Navigate to Web Form Page
def test_Navigate_To_Formy_Web_Form(browser):
    """ Act / WHEN Section """
    # Create an instanced Class object from the Web Form Page Class
    web_form_page = FormyWebFormPage(browser)

    # Call the Web Form Page load() method and navigate to the Web Form Page
    web_form_page.load()

    """ Assert / THEN Section """
    # Verify that the Web Form Page Heading Text matches the WEB_FORM_HEADING_TEXT variable
    assert web_form_page.web_form_heading_text() == WEB_FORM_HEADING_TEXT
