# Import Selenium locator modules for the Class Object to function
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Import the Page modules created in Pages folder
from pages.Formy_Home_Page import FormyHomePage

# Create a Class Object for the Formy Drag & Drop Page
class FormyDragDropPage(FormyHomePage):
    # Variables for each test related UI Element on the Formy Drag & Drop Page
    URL = 'https://formy-project.herokuapp.com/dragdrop'
    NAVIGATION_BAR_FORMY_TEXT = (By.ID, 'logo')
    DRAG_DROP_HEADING_TEXT = (By.TAG_NAME, 'h1')

    # Load the Formy Drag & Drop Page
    def load(self):
        self.browser.get(self.URL)

    # Find and return the Drag & Drop Pages Heading value for page load verification
    def drag_drop_heading_text(self):
        drag_drop_heading_value = self.browser.find_element(*self.DRAG_DROP_HEADING_TEXT)
        return drag_drop_heading_value.text