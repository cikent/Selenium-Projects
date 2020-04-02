# Import Selenium locator modules for the Class Object to function
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create a Class Object for the Formy Home Page
class FormyHomePage(object):
    # Create a String variable to hold the Formy Home Page address
    URL = 'https://formy-project.herokuapp.com/'

    # Variables for each test relevant UI element on the Formy Home Page
    NAVIGATION_BAR_FORMY_TEXT = (By.ID, 'logo')
    # HEADING_WELCOME_TEXT = (By.CLASS_NAME, 'jumbotron-fluid')

    # When the Class is instantiated, initialize the browser from the pytest fixture  
    def __init__(self, browser):
        self.browser = browser

    # Load the Formy Home Page
    def load(self):
        self.browser.get(self.URL)

    # Find and return the Greeting contained in the Formy Home Page Heading
    def home_greeting_text(self):
        heading1_value = self.browser.find_element(*self.HEADING_WELCOME_TEXT)
        return heading1_value.get_attribute('display-3')
