import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session") #we can also use scope as function, class, module. we can use this fixture across multiple test files as well
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture()
def page(browser):
    page = browser.new_page()
    yield page
    page.close()