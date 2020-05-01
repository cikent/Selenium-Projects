# Import Selenium locator modules for the Class Object to function
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Import the Page modules created in Pages folder
from pages.Formy_Home_Page import FormyHomePage

# Create a Class Object for the Formy Dropdown Page
class FormyDropdownPage(FormyHomePage):
    # Variables for each test related UI Element on the Formy Dropdown Page
    URL = 'https://formy-project.herokuapp.com/dropdown'
    NAVIGATION_BAR_FORMY_TEXT = (By.ID, 'logo')
    DROPDOWN_HEADING_TEXT = (By.TAG_NAME, 'h1')

    # Load the Formy Dropdown Page
    def load(self):
        self.browser.get(self.URL)

    # Find and return the Dropdown pages Heading value for load verification
    def dropdown_heading_text(self):
        dropdown_heading_value = self.browser.find_element(*self.DROPDOWN_HEADING_TEXT)
        return dropdown_heading_value.text
