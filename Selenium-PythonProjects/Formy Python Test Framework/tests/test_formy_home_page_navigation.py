# Import the Pytest
import pytest

# Import the Page modules created in Pages folder
from pages.Formy_Home_Page import FormyHomePage

# Define Test Function to Navigate to Formy Home Page
def test_Navigate_To_Formy_Home(browser):
    """ Arrange / GIVEN Section """
    # Assertion variables for each UI element on the Formy Home Page that will be verified           
    HOME_GREETING_TEXT = 'Welcome to Formy'                                                            

    """ Act / WHEN Section """
    # Create an instanced Class object from the FormyHomePage Class
    home_page = FormyHomePage(browser)
    # Call the FormyHomePage load() method and navigate to the Formy Home Page
    home_page.load()
    
    """ Assert / THEN Section """
    # Verify that the Formy Home Page Heading Text matches the GREETING value
    assert home_page.home_greeting_text == HOME_GREETING_TEXT
    