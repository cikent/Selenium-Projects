# Import Selenium locator modules for the Class Object to function
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Import the Page modules created in Pages folder
from pages.Formy_Home_Page import FormyHomePage

# Create a Class Object for the Formy File Upload Page
class FormyFileUploadPage(FormyHomePage):
    # Variables for each test related UI Element on the Formy File Upload Page
    URL = 'https://formy-project.herokuapp.com/fileupload'
    NAVIGATION_BAR_FORMY_TEXT = (By.ID, 'logo')
    FILE_UPLOAD_HEADING_TEXT = (By.TAG_NAME, 'h1')

    # Load the Formy File Upload Page
    def load(self):
        self.browser.get(self.URL)
    
    # Find and return the File Upload Page Heading value for page load verification
    def file_upload_heading_text(self):
        file_upload_heading_value = self.browser.find_element(*self.FILE_UPLOAD_HEADING_TEXT)
        return file_upload_heading_value.text

