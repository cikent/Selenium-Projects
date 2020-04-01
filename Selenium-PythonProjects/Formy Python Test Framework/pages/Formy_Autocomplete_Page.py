# Import Selenium locator modules for the Class Object to function
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Import the Page modules created in Pages folder
from pages.Formy_Home_Page import FormyHomePage

# Create a Class Object for the DuckDuckGo Home Page
class FormyAutocompletePage(object):
    # Create a String variable to hold the Formy Home Page value
    URL = 'https://formy-project.herokuapp.com/autocomplete'

    # When the Class is instantiated, initialize the browser from the pytest fixture  
    def __init__(self, browser):
        self.browser = browser

    # Load the Formy Home page
    def load(self):
        self.browser.get(self.URL)