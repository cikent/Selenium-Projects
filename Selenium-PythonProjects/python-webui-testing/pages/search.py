# Import Selenium Locator modules for the Class object to function
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create a Class Object for the DuckDuckGo home page
class DuckDuckGoSearchPage:
    # Create a String variable to hold the Duck Duck Go home page value
    URL = 'https://www.duckduckgo.com'

    # Create a Tuple variable to hold the Search Input text field Element Id value 
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

    # When the Class is instantiated, initialize the Browser from the pytest fixture  
    def __init__(self, browser):
        self.browser = browser

    # Load the DuckDuckGo home page
    def load(self):
        self.browser.get(self.URL)

    # Find the DuckDuckGo Search Input text field & pass in a phrase
    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
