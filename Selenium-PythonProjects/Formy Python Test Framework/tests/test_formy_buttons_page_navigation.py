# Import the Pytest Library
import pytest

# Import the Page modules created in Pages folder
from pages.ButtonsPagePo import ButtonsPage

""" Arrange / GIVEN Section """
# Assertion variables for each UI element on the Buttons Page that will be verified
PRIMARY_BUTTON = 'Primary'
SUCCESS_BUTTON = 'Success'
INFO_BUTTON = 'Info'
WARNING_BUTTON = 'Warning'
DANGER_BUTTON = 'Danger'
LINK_BUTTON = 'Link'
LEFT_BUTTON = 'Left'
MIDDLE_BUTTON = 'Middle'
RIGHT_BUTTON = 'Right'
ONE_BUTTON = '1'
TWO_BUTTON = '2'
DROPDOWN_MENU = 'Dropdown'

""" Act / WHEN Section """
# Create an instanced Class object from the Buttons Page Class
""" buttons_page = ButtonsPage(browser)

# Call the Buttons Page load() method and navigate to the Buttons Page
buttons_page.load() """

# Define Test Function to Navigate to Buttons Page
def ButtonsPageSetup(browser):
    """ Act / WHEN Section """
    # Create an instanced Class object from the Buttons Page Class
    buttons_page = ButtonsPage(browser)

    # Call the Buttons Page load() method and navigate to the Buttons Page
    buttons_page.load()

    # Return the Buttons Page
    return buttons_page

# Define Test Function to Navigate to Buttons Page
def test_Primary_Button_Selection_Via_XPATH(browser):
    """ Act / WHEN Section """
    # Create an instanced Class object from the Buttons Page Class
    ButtonsPageSetup(browser)

    """ Assert / THEN Section """
    # Verify that the Buttons Page Primary Button text matches the Primary Buttons variable value
    assert buttons_page.primary_button_xpath(buttons_page) == PRIMARY_BUTTON

# Define Test Function to Navigate to Buttons Page
def test_Navigate_To_Formy_Buttons(browser):
    """ Act / WHEN Section """
    # Create an instanced Class object from the Buttons Page Class
    buttons_page = ButtonsPage(browser)

    # Call the Buttons Page load() method and navigate to the Buttons Page
    buttons_page.load()

    """ Assert / THEN Section """
    # Verify that the Buttons Page Primary Button text matches the Primary Buttons variable value
    assert buttons_page.primary_button_xpath() == PRIMARY_BUTTON
    