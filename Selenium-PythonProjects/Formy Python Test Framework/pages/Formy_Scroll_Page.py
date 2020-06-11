# Import Selenium locator modules for the Class Object to function
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Import the Page modules created in Pages folder
from pages.Formy_Home_Page import FormyHomePage

# Create a Class Object for the Formy Scroll Page
class FormyScrollPage(FormyHomePage):
    # Variables for each test related UI Element on the Formy Scroll Page
    URL = 'https://formy-project.herokuapp.com/scroll'
    NAVIGATION_BAR_FORMY_TEXT = (By.ID, 'logo')
    SCROLL_HEADING_TEXT = (By.TAG_NAME, 'h1')

    # Load the Formy Scroll Page
    def load(self):
        self.browser.get(self.URL)

    # Find and return the Scroll Page Heading value for page load verification
    def scroll_heading_text(self):
        scroll_heading_value = self.browser.find_element(*self.SCROLL_HEADING_TEXT)
        return scroll_heading_value.text

