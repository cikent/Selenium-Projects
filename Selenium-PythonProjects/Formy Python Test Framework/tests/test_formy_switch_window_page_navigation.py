# Import the Pytest Library
import pytest

# Import the Page modules created in Pages folder
from pages.Formy_Switch_Window_Page import FormySwitchWindowPage

""" Arrange / GIVEN Section """
# Assertion variables for each UI element on the Sub-Page that will be verified
SWITCH_WINDOW_HEADING_TEXT = 'Switch Window'

# Define Test Function to Navigate to Switch Window Page
def test_Navigate_To_Formy_Switch_Window(browser):
    """ Act / WHEN Section """
    # Create an instanced Class object from the Switch Window Page Class
    switch_window_page = FormySwitchWindowPage(browser)

    # Call the Switch Window Page load() method and navigate to the Switch Window Page
    switch_window_page.load()

    """ Assert / THEN Section """
    # Verify that the Switch Window Page Heading Text matches the SWITCH_WINDOW_HEADING_TEXT variable
    assert switch_window_page.switch_window_heading_text() == SWITCH_WINDOW_HEADING_TEXT
