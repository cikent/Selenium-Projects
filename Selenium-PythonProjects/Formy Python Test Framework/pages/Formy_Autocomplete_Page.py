# Import Selenium locator modules for the Class Object to function
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Import the Page modules created in Pages folder
from pages.Formy_Home_Page import FormyHomePage

# Create a Class Object for the Formy Autocomplete Page
class FormyAutocompletePage(FormyHomePage):
    # Variables for each test related UI Element on the Formy Autocomplete Page
    URL = 'https://formy-project.herokuapp.com/autocomplete'
    NAVIGATION_BAR_FORMY_TEXT = (By.ID, 'logo')
    AUTOCOMPLETE_HEADING_TEXT = (By.TAG_NAME, 'h1')

    # Load the Formy Autocomplete Page
    def load(self):
        self.browser.get(self.URL)

    # Find and return the Autocomplete Pages Heading value for page load verification
    def autocomplete_heading_text(self):
        autocomplete_heading_value = self.browser.find_element(*self.AUTOCOMPLETE_HEADING_TEXT)
        return autocomplete_heading_value.text