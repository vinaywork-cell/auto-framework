class LoginPage:
    def __init__(self, page):
        self.page = page

    def enter_email(self, email):
        self.page.get_by_role('textbox', name='Email Id').fill(email)

    def enter_password(self, password):
        self.page.get_by_role('textbox', name='Password').fill(password)

    def click_login(self):
        self.page.get_by_role('button', name='Login').click()

    def click_myteam(self):
        self.page.get_by_role('link', name=' MyTeam').click()