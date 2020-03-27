# Import Selenium Locator modules for the Class Object to function
from selenium.webdriver.common.by import By

# Create a Class Object for the DuckDuckGo Results page
class DuckDuckGoResultPage(object):
    # Create a Tuple variable to hold the List of links returned using a CSS Selector for the 'div' called: links 
    LINK_DIVS = (By.CSS_SELECTOR, '#links > div')
    # Create a Tuple variable to hold the Search Input Text Field using the Element Id value named 'search_form_input'
    SEARCH_INPUT = (By.ID, 'search_form_input')

    # Create a Static Method that will only work within the Class Object
    @classmethod
    # Look for the search phrase passed in the 'div' called: links on the Results page
    def PHRASE_RESULTS(cls, phrase):
        xpath = f"//div[@id='links']//*[contains(text(), '{phrase}')]"
        return (By.XPATH, xpath)

    # When the Class is instantiated, initialize the browser from the pytest fixture
    def __init__(self, browser):
        self.browser = browser

    # Find and return the # of links displayed on the Results page
    def link_div_count(self):
        link_divs = self.browser.find_elements(*self.LINK_DIVS)
        return len(link_divs)

    # Find and return the # of links displayed that match the search phrase on the Results page
    def phrase_result_count(self, phrase):
        phrase_results = self.browser.find_elements(*self.PHRASE_RESULTS(phrase))
        return len(phrase_results)
    
    # Find and and return the value contained in the Search Text Field on the Results page
    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')