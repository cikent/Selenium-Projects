# Import Selenium locator modules for the Class Object to function
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Import the Page modules created in Pages folder
from pages.Formy_Home_Page import FormyHomePage

# Create a Class Object for the Formy Autocomplete Page
class FormyAutocompletePage(FormyHomePage):
    # Create a String variable to hold the Formy Autocomplete Page address
    URL = 'https://formy-project.herokuapp.com/autocomplete'

    # Load the Formy Autocomplete Page
    def load(self):
        self.browser.get(self.URL)
