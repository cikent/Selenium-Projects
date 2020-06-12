# Import the Pytest Library
import pytest

# Import the Page modules created in Pages folder
from pages.Formy_Radio_Buttons_Page import FormyRadioButtonsPage

""" Arrange / GIVEN Section """
# Assertion variables for each UI element on the Radio Buttons Page that will be verified
RADIO_BUTTONS_HEADING_TEXT = 'Radio buttons'

# Define Test Function to Navigate to Radio Buttons Page
def test_Navigate_To_Formy_Radio_Button(browser):
    """ Act / WHEN Section """
    # Create an instanced Class object from the Radio Buttons Page Class
    radio_buttons_page = FormyRadioButtonsPage(browser)

    # Call the Radio Buttons Page load() method and navigate to the Radio Buttons Page
    radio_buttons_page.load()

    """ Assert / THEN Section """
    # Verify that the Radio Buttons Page Heading Text matches the _HEADING_TEXT variable
    assert radio_buttons_page.radio_buttons_heading_text() == RADIO_BUTTONS_HEADING_TEXT
