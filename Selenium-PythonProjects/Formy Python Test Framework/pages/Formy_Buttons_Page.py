# Import Selenium locator modules for the Class Object to function
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Import the Page modules created in Pages folder
from pages.Formy_Home_Page import FormyHomePage

# Create a Class Object for the Formy Buttons Page
class FormyButtonsPage(FormyHomePage):
    # Create a String variable to hold the Formy Buttons Page address
    URL = 'https://formy-project.herokuapp.com/buttons'

    # Load the Formy Buttons Page
    def load(self):
        self.browser.get(self.URL)
