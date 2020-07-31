# Import Selenium locator modules for the Class Object to function
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create a Class for the Formy Home Page
class FormyHomePage(object):
    # Define and assign the Element Locator Variables for each test related UI Element on the Formy Home Page
    """
    Element Locator Variable Convention Requirements:
    - All Cap Letters
    - Each word seperated by Underscores
    - First Word = The on-screen element name
    - Second Word (optional) = Descriptive word respective to the elements location on-screen
    - Third Word = The type of element
    - Example Source URL: "https://formy-project.herokuapp.com/buttons"
    - Example(s):
        - PRIMARY_BUTTON: There is only one "Primary" button on-screen, so the need to be descriptive about its location isn't relevant for this page. 
        - FORMY_NAVIGATION_BAR_TEXT: There are multiple spots on the page with the word "Formy", so it's necessary to be more descriptive about its location (do you see both locations?).
    """
    URL = 'https://formy-project.herokuapp.com/'
    FORMY_NAVIGATION_BAR_TEXT = (By.ID, 'logo')
    WELCOME_GREETING_TEXT = (By.CLASS_NAME, 'display-3')

    # When the Class is instantiated, initialize the browser from the pytest fixture  
    def __init__(self, browser):
        self.browser = browser

    # Load the Formy Home Page
    def load(self):
        self.browser.get(self.URL)

    # Find and return the Greeting Text displayed on the Formy Home Page
    def welcome_greeting_text(self):
        welcome_greeting_value = self.browser.find_element(
            *self.WELCOME_GREETING_TEXT)
        return welcome_greeting_value.text
