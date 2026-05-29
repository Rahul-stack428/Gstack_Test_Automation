from playwright.sync_api import expect
from pages.login_page import LoginPage


def test_valid_login(page):
    page_obj = LoginPage(page)
    page_obj.email_input.fill('valid_email')
    page_obj.password_input.fill('valid_password')
    page_obj.sign_in_button.click()
    expect(page).to_have_url('**/dashboard')

def test_invalid_password(page):
    page_obj = LoginPage(page)
    page_obj.email_input.fill('valid_email')
    page_obj.password_input.fill('invalid_password')
    page_obj.sign_in_button.click()
    expect(page.get_by_text('Invalid credentials')).to_be_visible()

def test_invalid_email(page):
    page_obj = LoginPage(page)

def test_blank_email(page):
    page_obj = LoginPage(page)

def test_blank_password(page):
    page_obj = LoginPage(page)
