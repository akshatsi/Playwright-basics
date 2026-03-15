import re
from playwright.sync_api import Page, expect
from pages.orangehrm_login import Login
from pages.orangehrm_home_page import HomePage



def test_example(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login = Login(page)
    login.enter_username("Admin")
    login.enter_password("admin123")
    login.click_login()
    home_page = HomePage(page)
    home_page.is_upgrade_button_visible()
    home_page.click_performance_link()
    home_page.click_dashboard_link()
