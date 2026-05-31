from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

        self.email_input = page.locator('[name="email"]')

        self.password_input = page.locator('[name="password"]')

        self.sign_in_button = page.locator('text="Sign In"')

        self.email_address = page.locator('text="Email Address*"')

        self.password = page.locator('text="Password*"')

        self.terms = page.locator('text="Terms"')

        self.privacy_policy = page.locator('text="Privacy Policy"')

        self.sign_in_email_address_password_remember_mereset_nowsign_inby_signing_in_i_accept_theterms_privacy_policy = page.locator('text="Sign In!Email Address*Password*Remember MeReset NowSign InBy Signing In , I accept theTerms& Privacy Policy"')

        self.sign_in = page.locator('text="Sign In!"')

        self.remember_me = page.locator('text="Remember Me"')

        self.reset_now = page.locator('text="Reset Now"')

        self.by_signing_in_i_accept_the = page.locator('text="By Signing In , I accept the"')

        self.terms = page.locator('text="Terms"')

        self.privacy_policy = page.locator('text="Privacy Policy"')

        self.email_address = page.locator('text="Email Address*"')

        self.password = page.locator('text="Password*"')

        self.remember_me = page.locator('text="Remember Me"')

    def login(self, username, password):
        self.email.fill(username)
        self.password.fill(password)
        self.sign_in.click()
        self.page.wait_for_load_state('networkidle')

    def login(self, username, password):
        self.email.fill(username)
        self.password.fill(password)
        self.sign_in.click()
