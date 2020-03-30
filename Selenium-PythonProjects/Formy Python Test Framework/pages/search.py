# Import Selenium locator modules for the Class Object to function
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create a Class Object for the DuckDuckGo Home page
class DuckDuckGoSearchPage(object):
    # Create a String variable to hold the Duck Duck Go Home page value
    URL = 'https://www.duckduckgo.com'

    # Create a Tuple variable to hold the Search Input Text Field using the Element Id value named 'search_form_input_homepage'
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

    # When the Class is instantiated, initialize the browser from the pytest fixture  
    def __init__(self, browser):
        self.browser = browser

    # Load the DuckDuckGo Home page
    def load(self):
        self.browser.get(self.URL)

    # Find the DuckDuckGo Search Input Text Field & pass in a phrase
    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
