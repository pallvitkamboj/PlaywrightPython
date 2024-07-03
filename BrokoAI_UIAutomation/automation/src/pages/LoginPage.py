class LoginPage:

    def __init__(self, page):
        self.page = page
        self.inputUsername = page.get_by_label("Email")
        self.inputPassword = page.get_by_label("Password")
        self.loginButton = page.get_by_role("button", name="Login")
        self.homeTitle = page.locator("h1[class='page-title']")