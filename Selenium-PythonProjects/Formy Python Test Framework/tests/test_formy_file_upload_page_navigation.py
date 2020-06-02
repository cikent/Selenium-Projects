# Import the Pytest Library
import pytest

# Import the Page modules created in Pages folder
from pages.Formy_File_Upload_Page import FormyFileUploadPage

""" Arrange / GIVEN Section """
# Assertion variables for each UI element on the Sub-Page that will be verified
FILE_UPLOAD_HEADING_TEXT = 'File upload'

# Define Test Function to Navigate to File Upload Page
def test_Navigate_To_Formy_File_Upload(browser):
    """ Act / WHEN Section """
    # Create an instanced Class object from the File Upload Page Class
    file_upload_page = FormyFileUploadPage(browser)

    # Call the File Upload Page load() method and navigate to the File Upload Page
    file_upload_page.load()

    """ Assert / THEN Section """
    # Verify that the File Upload Page Heading Text matches the FILE_UPLOAD_HEADING_TEXT variable
    assert file_upload_page.file_upload_heading_text() == FILE_UPLOAD_HEADING_TEXT
