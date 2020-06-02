# Import Selenium locator modules for the Class Object to function
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Import the Page modules created in Pages folder
from pages.Formy_Home_Page import FormyHomePage

# Create a Class Object for the Formy Keyboard & Mouse Input Page
class FormyKeyboardMouseInputPage(FormyHomePage):
    # Variables for each test related UI Element on the Formy Keyboard & Mouse Input Page
    URL = 'https://formy-project.herokuapp.com/keypress'
    NAVIGATION_BAR_FORMY_TEXT = (By.ID, 'logo')
    KEYBOARD_MOUSE_HEADING_TEXT = (By.TAG_NAME, 'h1')

    # Load the Formy Keyboard & Mouse Input Page
    def load(self):
        self.browser.get(self.URL)

    # Find and return the Keyboard & Mouse Input Page Heading value for page load verification
    def keyboard_mouse_heading_text(self):
        keyboard_mouse_heading_value = self.browser.find_element(*self.KEYBOARD_MOUSE_HEADING_TEXT)
        return keyboard_mouse_heading_value.text
