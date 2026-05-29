from playwright.sync_api import expect
from utils.data_loader import DataLoader
from pages.login_page import LoginPage


def test_valid_login(page):
    page_obj = LoginPage(page)
    data = DataLoader.load('login_data.json')
    page_obj.fill(page_obj.email_input, data['valid_email'])
    page_obj.fill(page_obj.password_input, data['valid_password'])
    page_obj.click(page_obj.sign_in_button)
    expect(page).to_have_url('**/dashboard')

def test_invalid_password(page):
    page_obj = LoginPage(page)
    data = DataLoader.load('login_data.json')
    page_obj.fill(page_obj.email_input, data['valid_email'])
    page_obj.fill(page_obj.password_input, data['invalid_password'])
    page_obj.click(page_obj.sign_in_button)
    expect(page.get_by_text('Invalid credentials')).to_be_visible()

def test_invalid_email(page):
    page_obj = LoginPage(page)
    data = DataLoader.load('login_data.json')

def test_blank_email(page):
    page_obj = LoginPage(page)
    data = DataLoader.load('login_data.json')

def test_blank_password(page):
    page_obj = LoginPage(page)
    data = DataLoader.load('login_data.json')
