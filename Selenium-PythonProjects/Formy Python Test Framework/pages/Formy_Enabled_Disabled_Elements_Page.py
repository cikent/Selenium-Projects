# Import Selenium locator modules for the Class Object to function
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Import the Page modules created in Pages folder
from pages.Formy_Home_Page import FormyHomePage

# Create a Class Object for the Formy Enabled & Disabled Elements Page
class FormyEnabledDisabledElementsPage(FormyHomePage):
    # Variables for each test related UI Element on the Formy Enabled & Disabled Elements Page
    URL = 'https://formy-project.herokuapp.com/enabled'
    NAVIGATION_BAR_FORMY_TEXT = (By.ID, 'logo')
    ENABLE_DISABLE_HEADING_TEXT = (By.TAG_NAME, 'h1')

    # Load the Formy Enabled & Disabled Elements Page
    def load(self):
        self.browser.get(self.URL)

    # Find and return the Enable and Disable pages Heading value for load verification
    def enable_disable_heading_text(self):
        enable_disable_heading_value = self.browser.find_element(*self.ENABLE_DISABLE_HEADING_TEXT)
        return enable_disable_heading_value.text

