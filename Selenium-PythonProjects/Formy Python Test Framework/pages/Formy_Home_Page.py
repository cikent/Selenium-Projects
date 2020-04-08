# Import Selenium locator modules for the Class Object to function
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create a Class Object for the Formy Home Page
class FormyHomePage(object):
    # Create a String variable to hold the Formy Home Page address
    URL = 'https://formy-project.herokuapp.com/'

    # Variables for each test relevant UI element on the Formy Home Page
    NAVIGATION_BAR_FORMY_TEXT = (By.ID, 'logo')
    HOME_GREETING_TEXT = (By.CLASS_NAME, 'display-3')

    # When the Class is instantiated, initialize the browser from the pytest fixture  
    def __init__(self, browser):
        self.browser = browser

    # Load the Formy Home Page
    def load(self):
        self.browser.get(self.URL)

    # Find and return the Greeting Text displaed on the Formy Home Page
    def home_greeting_text(self):
        home_greeting_value = self.browser.find_element(*self.HOME_GREETING_TEXT)
        return home_greeting_value.get
