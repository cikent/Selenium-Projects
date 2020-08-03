# Import the Pytest Library
import pytest

# Import the Buttons Page module created in Pages folder
from pages.ButtonsPagePo import ButtonsPage

""" Arrange / GIVEN Section """
# Assertion/Test variables for tests on the Buttons Page
BUTTONS_PAGE_TITLE = 'Formy'
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

# Setup function for Buttons Page
def buttonsPageSetup(browser):
    # Create an instanced Class object from the Buttons Page Class
    buttons_page = ButtonsPage(browser)

    # Call the Buttons Page load() method and navigate to the Buttons Page
    buttons_page.load()

    # Return the Buttons Page Object
    return buttons_page

# Verify Buttons Page has loaded in the browser
def test_Buttons_Page_Load(browser):
    """ Arrange / GIVEN Section """
    # Create an instance of Buttons page using the setup function
    buttons_page = buttonsPageSetup(browser)

    """ Act / WHEN Section """
    # Create a Title object(variable) using (Selenium)
    buttons_page_title = browser.title
    
    """ Assert / THEN Section """
    # Verify the Buttons Page Title matches the BUTTONS_PAGE_TITLE variable value
    assert buttons_page_title == BUTTONS_PAGE_TITLE

# Verify Buttons Page has a button called: Primary Button
def test_Primary_Button_Selection_Via_ABS_XPATH(browser):
    """ Arrange / GIVEN Section """
    # Create an instance of Buttons page using the setup function
    buttons_page = buttonsPageSetup(browser)
    
    """ Act / WHEN Section """
    # Create a Button object(variable) using the XPATH Element Locator to interact with
    primary_button = buttons_page.primary_button_abs_xpath()

    """ Assert / THEN Section """
    # Verify the Buttons Page function "primary_button_xpath()" accurately locates the Primary Button element by verifying Text value
    assert primary_button.text == PRIMARY_BUTTON

# Verify Buttons Page has a button called: Primary Button
def test_Primary_Button_Selection_Via_REL_XPATH(browser):
    """ Arrange / GIVEN Section """
    # Create an instance of Buttons page using the setup function
    buttons_page = buttonsPageSetup(browser)
    
    """ Act / WHEN Section """
    # Create a Button object(variable) using the XPATH Element Locator to interact with
    primary_button = buttons_page.primary_button_rel_xpath()

    """ Assert / THEN Section """
    # Verify the Buttons Page function "primary_button_xpath()" accurately locates the Primary Button element by verifying Text value
    assert primary_button.text == PRIMARY_BUTTON
