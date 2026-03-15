from playwright.sync_api import Page, expect
class Login:
    def __init__(self,page:Page):
        self.page = page
        self.username = page.get_by_role("textbox", name="Username")
        self.password = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

    def enter_username(self,username:str):

        self.username.fill(username)
    def enter_password(self,password:str):
        self.password.fill(password)
    def click_login(self):
        self.login_button.click()