# Import Selenium locator modules for the Class Objects to function
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Import the Page modules created in Pages folder
from pages.FormyHomePagePo import FormyHomePage

# Create a Class for the Buttons Page
class ButtonsPage(FormyHomePage):
    # Define and assign the Element Locator Variables for each test related UI Elements on the Buttons Page
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
    URL = 'https://formy-project.herokuapp.com/buttons'
    FORMY_NAVIGATION_BAR_TEXT = (By.ID, 'logo')
    PRIMARY_BUTTON_XPATH = (By.XPATH, '/html/body/div/form/div[1]/div/div/button[1]')

    # Load the Buttons Page
    def load(self):
        self.browser.get(self.URL)

    # Element Locator: Return the Primary Button Element via XPATH
    def primary_button_xpath(self):
        primary_button_element = self.browser.find_element(*self.PRIMARY_BUTTON_XPATH)
        return primary_button_element
