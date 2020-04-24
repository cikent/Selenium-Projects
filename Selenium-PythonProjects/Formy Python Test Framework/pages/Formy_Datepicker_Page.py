# Import Selenium locator modules for the Class Object to function
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Import the Page modules created in Pages folder
from pages.Formy_Home_Page import FormyHomePage

# Create a Class Object for the Formy Datepicker Page
class FormyDatepickerPage(FormyHomePage):
    # Variables for each test related UI Element on the Formy Datepicker Page
    URL = 'https://formy-project.herokuapp.com/datepicker'

    # Load the Formy Datepicker Page
    def load(self):
        self.browser.get(self.URL)
