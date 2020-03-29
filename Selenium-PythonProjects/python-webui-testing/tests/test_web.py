# Import the Pytest
import pytest

# Import the Page modules created in Pages folder
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

# Define Test Function to Search DuckDuckGo
def test_basic_duckduckgo_search(browser):
    """ Arrange / GIVEN Section """
    # Define a test specifc search phrase (i.e. Set up test case data)               
    PHRASE = 'panda'                                                            

    """ Act / WHEN Section """
    # Create an instanced Class object from the DuckDuckGoSearchPage Class
    search_page = DuckDuckGoSearchPage(browser)
    # Call the DuckDuckGoSearchPage Load method and navigate to the Duck Duck Go home page
    search_page.load()
    # Find the Search Text field and pass in the Search
    search_page.search(PHRASE)

    """ Assert / THEN Section """
    # Create an instanced Class object from the DuckDuckGoResultsPage Class
    results_page = DuckDuckGoResultPage(browser)
    # Verify the 'div' called Links returns more than zero links
    assert results_page.link_div_count() > 0
    # Verify the 'div' called Links returns more than zero links that match the search phrase value
    assert results_page.phrase_result_count(PHRASE) > 0
    # Verify that the Results page Search Text Field value matches the search phrase
    assert results_page.search_input_value() == PHRASE

