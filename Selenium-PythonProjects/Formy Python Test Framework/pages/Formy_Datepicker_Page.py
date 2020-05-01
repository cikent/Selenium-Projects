# Import Selenium locator modules for the Class Object to function
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Import the Page modules created in Pages folder
from pages.Formy_Home_Page import FormyHomePage

# Create a Class Object for the Formy Datepicker Page
class FormyDatepickerPage(FormyHomePage):
    # Variables for each test related UI Element on the Formy Datepicker Page
    URL = 'https://formy-project.herokuapp.com/datepicker'
    NAVIGATION_BAR_FORMY_TEXT = (By.ID, 'logo')
    DATEPICKER_HEADING_TEXT = (By.TAG_NAME, 'h1')

    # Load the Formy Datepicker Page
    def load(self):
        self.browser.get(self.URL)

    # Find and return the Datepicker Pages Heading value for page load verification
    def datepicker_heading_text(self):
        datepicker_heading_value = self.browser.find_element(*self.DATEPICKER_HEADING_TEXT)
        return datepicker_heading_value.text

