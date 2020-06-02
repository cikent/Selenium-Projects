# Import the Pytest Library
import pytest

# Import the Page modules created in Pages folder
from pages.Formy_Keyboard_Mouse_Input_Page import FormyKeyboardMouseInputPage

""" Arrange / GIVEN Section """
# Assertion variables for each UI element on the Formy Formy Keyboard & Mouse Input Page that will be verified
KEYBOARD_MOUSE_HEADING_TEXT = 'Keyboard and Mouse Input'

# Define Test Function to Navigate to Formy Formy Keyboard & Mouse Input Page
def test_Navigate_To_Formy_Keyboard_Mouse(browser):
    """ Act / WHEN Section """
    # Create an instanced Class object from the FormyKeyboardMouseInputPage Class
    keyboard_mouse_page = FormyKeyboardMouseInputPage(browser)
    # Call the FormyDragDropPage load() method and navigate to the Formy Formy Keyboard & Mouse Input Page
    keyboard_mouse_page.load()

    """ Assert / THEN Section """
    # Verify that the Formy Formy Keyboard & Mouse Input Page Heading Text matches the KEYBOARD_MOUSE_HEADING_TEXT variable
    assert keyboard_mouse_page.keyboard_mouse_heading_text() == KEYBOARD_MOUSE_HEADING_TEXT