# Import the Pytest Library
import pytest

# Import the modules created in the Pages folder
from pages.EnabledDisabledElementsPagePo import EnabledDisabledElementsPage

""" Arrange / GIVEN Section """
# Assertion variables for each UI element on the Formy Enable & Disable Page that will be verified
ENABLE_DISABLE_HEADING_TEXT = 'Enabled and Disabled elements'

# Define Test Function to Navigate to Formy Enable & Disable Page
def test_Navigate_To_Formy_Enable_Disable(browser):
    """ Act / WHEN Section """
    # Create an instanced Class object from the FormyEnableDisablePage Class
    enable_disable_page = EnabledDisabledElementsPage(browser)
    # Call the FormyEnableDisablePage load() method and navigate to the Formy Enable & Disable Page
    enable_disable_page.load()

    """ Assert / THEN Section """
    # Verify that the Formy Enable & Disable Page Heading Text matches the ENABLE_DISABLE_HEADING_TEXT variable
    assert enable_disable_page.enable_disable_heading_text() == ENABLE_DISABLE_HEADING_TEXT
