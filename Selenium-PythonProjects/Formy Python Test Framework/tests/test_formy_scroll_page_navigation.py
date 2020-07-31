# Import the Pytest Library
import pytest

# Import the Page modules created in Pages folder
from pages.PageScrollPagePo import PageScrollPage

""" Arrange / GIVEN Section """
# Assertion variables for each UI element on the Scroll Page that will be verified
PAGE_SCROLL_HEADING_TEXT = 'Large page content'

# Define Test Function to Navigate to Scroll Page
def test_Navigate_To_Formy_Scroll(browser):
    """ Act / WHEN Section """
    # Create an instanced Class object from the Scroll Page Class
    page_scroll_page = PageScrollPage(browser)

    # Call the Scroll Page load() method and navigate to the Scroll Page
    page_scroll_page.load()

    """ Assert / THEN Section """
    # Verify that the Scroll Page Heading Text matches the SCROLL_HEADING_TEXT variable
    assert page_scroll_page.scroll_heading_text() == PAGE_SCROLL_HEADING_TEXT
