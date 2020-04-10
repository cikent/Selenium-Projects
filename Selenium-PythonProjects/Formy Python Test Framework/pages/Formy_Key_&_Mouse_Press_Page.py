# Import Selenium locator modules for the Class Object to function
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Import the Page modules created in Pages folder
from pages.Formy_Home_Page import FormyHomePage

# Create a Class Object for the Formy Keypress & Mouse Input Page
class FormyKeyAndMouseInputPage(FormyHomePage):
    # Create a String variable to hold the Formy Keypress & Mouse Input Page address
    URL = 'https://formy-project.herokuapp.com/keypress'

    # Load the Formy Keypress & Mouse Input Page
    def load(self):
        self.browser.get(self.URL)
