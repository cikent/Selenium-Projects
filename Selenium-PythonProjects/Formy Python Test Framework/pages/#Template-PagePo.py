# Import Selenium locator modules for the Class Object to function

# Import the Page modules created in Pages folder

# Create a Class Object for the Sub-Page

# Define and assign the Element Locator Variables for each test related UI Element on the Sub-Page
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
  
# Load the Sub-Page

# Find and return the Sub-Page Heading value for page load verification
