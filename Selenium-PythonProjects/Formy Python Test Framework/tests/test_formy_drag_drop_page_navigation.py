# Import the Pytest Library
import pytest

# Import the Page modules created in Pages folder
from pages.Formy_Drag_Drop_Page import FormyDragDropPage

""" Arrange / GIVEN Section """
# Assertion variables for each UI element on the Formy Drag & Drop Page that will be verified
DRAG_DROP_HEADING_TEXT = 'Drag the image into the box'

# Define Test Function to Navigate to Formy Drag & Drop Page
def test_Navigate_To_Formy_Drag_Drop(browser):
    """ Act / WHEN Section """
    # Create an instanced Class object from the FormyDragDropPage Class
    drag_drop_page = FormyDragDropPage(browser)
    # Call the FormyDragDropPage load() method and navigate to the Formy Drag & Drop Page
    drag_drop_page.load()

    """ Assert / THEN Section """
    # Verify that the Formy Drag & Drop Page Heading Text matches the DRAG_DROP_HEADING_TEXT variable
    assert drag_drop_page.drag_drop_heading_text() == DRAG_DROP_HEADING_TEXT
