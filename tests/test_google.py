import re
from playwright.sync_api import expect
from playwright.sync_api._generated import Page

def test_google_title(page: Page):
    page.wait_for_timeout(3000)  # Wait for 3 seconds to ensure the page is fully loaded
    page.goto("https://www.google.com")
    try:
        page.get_by_role("button", name="Accept all").click(timeout=5000)

    except:
        print("No popup found")

    page.get_by_role("combobox", name="Search").fill("Playwright python")
    page.keyboard.press("Enter")

    
    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))