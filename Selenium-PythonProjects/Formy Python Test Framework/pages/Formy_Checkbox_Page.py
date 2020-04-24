# Import Selenium locator modules for the Class Object to function
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Import the Page modules created in Pages folder
from pages.Formy_Home_Page import FormyHomePage

# Create a Class Object for the Formy Checkbox Page
class FormyCheckboxPage(FormyHomePage):
    # Variables for each test related UI Element on the Formy Checkbox Page
    URL = 'https://formy-project.herokuapp.com/checkbox'
    NAVIGATION_BAR_FORMY_TEXT = (By.ID, 'logo')
    CHECKBOX_HEADING_TEXT = (By.TAG_NAME, 'h1')
    
    # Load the Formy Checkbox Page
    def load(self):
        self.browser.get(self.URL)

    # Find and return the Checkbox Pages Heading value for page load verification
    def checkbox_heading_text(self):
        checkbox_heading_value = self.browser.find_element(*self.CHECKBOX_HEADING_TEXT)
        return checkbox_heading_value.text
