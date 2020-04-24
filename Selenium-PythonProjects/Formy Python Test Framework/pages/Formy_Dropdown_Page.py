# Import Selenium locator modules for the Class Object to function
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Import the Page modules created in Pages folder
from pages.Formy_Home_Page import FormyHomePage

# Create a Class Object for the Formy Dropdown Page
class FormyDropdownPage(FormyHomePage):
    # Variables for each test related UI Element on the Formy Dropdown Page
    URL = 'https://formy-project.herokuapp.com/dropdown'

    # Load the Formy Dropdown Page
    def load(self):
        self.browser.get(self.URL)
