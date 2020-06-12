# Import Selenium locator modules for the Class Object to function
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Import the Page modules created in Pages folder
from pages.Formy_Home_Page import FormyHomePage

# Create a Class Object for the Formy Switch Window Page
class FormySwitchWindowPage(FormyHomePage):
    # Variables for each test related UI Element on the Formy Switch Window Page
    URL = 'https://formy-project.herokuapp.com/switch-window'
    NAVIGATION_BAR_FORMY_TEXT = (By.ID, 'logo')
    SWITCH_WINDOW_HEADING_TEXT = (By.TAG_NAME, 'h1')

    # Load the Formy Switch Window Page
    def load(self):
        self.browser.get(self.URL)

    # Find and return the Switch Window Page Heading value for page load verification
    def switch_window_heading_text(self):
        switch_window_heading_value = self.browser.find_element(*self.SWITCH_WINDOW_HEADING_TEXT)
        return switch_window_heading_value.text
