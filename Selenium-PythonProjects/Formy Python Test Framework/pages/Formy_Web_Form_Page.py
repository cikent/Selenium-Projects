# Import Selenium locator modules for the Class Object to function
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Import the Page modules created in Pages folder
from pages.Formy_Home_Page import FormyHomePage

# Create a Class Object for the Formy Web Form Page
class FormyWebFormPage(FormyHomePage):
    # Variables for each test related UI Element on the Formy Web Form Page
    URL = 'https://formy-project.herokuapp.com/form'
    NAVIGATION_BAR_FORMY_TEXT = (By.ID, 'logo')
    WEB_FORM_HEADING_TEXT = (By.TAG_NAME, 'h1')

    # Load the Formy Web Form Page
    def load(self):
        self.browser.get(self.URL)

    # Find and return the Web Form Page Heading value for page load verification
    def web_form_heading_text(self):
        web_form_heading_value = self.browser.find_element(*self.WEB_FORM_HEADING_TEXT)
        return web_form_heading_value.text
