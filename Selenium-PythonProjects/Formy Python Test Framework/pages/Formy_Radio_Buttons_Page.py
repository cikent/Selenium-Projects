# Import Selenium locator modules for the Class Object to function
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Import the Page modules created in Pages folder
from pages.Formy_Home_Page import FormyHomePage

# Create a Class Object for the Formy Radio Buttons Page
class FormyRadioButtonsPage(FormyHomePage):
    # Variables for each test related UI Element on the Formy Radio Buttons Page
    URL = 'https://formy-project.herokuapp.com/radiobutton'
    NAVIGATION_BAR_FORMY_TEXT = (By.ID, 'logo')
    RADIO_BUTTONS_HEADING_TEXT = (By.TAG_NAME, 'h1')

    # Load the Formy Radio Buttons Page
    def load(self):
        self.browser.get(self.URL)

    # Find and return the Radio Buttons Page Heading value for page load verification
    def radio_buttons_heading_text(self):
        radio_buttons_heading_value = self.browser.find_element(*self.RADIO_BUTTONS_HEADING_TEXT)
        return radio_buttons_heading_value.text
