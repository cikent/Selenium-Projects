# Import Selenium locator modules for the Class Object to function
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Import the Page modules created in Pages folder
from pages.FormyHomePagePo import FormyHomePage

# Create a Class Object for the File Upload Page
class FileUploadPage(FormyHomePage):
    # Define and assign the Element Locator Variables for each test related UI Element on the File Upload Page
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
    URL = 'https://formy-project.herokuapp.com/fileupload'
    FORMY_NAVIGATION_BAR_TEXT = (By.ID, 'logo')
    FILE_UPLOAD_HEADING_TEXT = (By.TAG_NAME, 'h1')

    # Load the File Upload Page
    def load(self):
        self.browser.get(self.URL)
    
    # Find and return the File Upload Page Heading value for page load verification
    def file_upload_heading_text(self):
        file_upload_heading_value = self.browser.find_element(*self.FILE_UPLOAD_HEADING_TEXT)
        return file_upload_heading_value.text

