from playwright.sync_api import expect
from utils.data_loader import DataLoader
from pages.generic_page import GenericPage


def test_select_platform_admin(page):
    page_obj = GenericPage(page)
    data = DataLoader.load('login_data.json')
    expect(page).to_have_url('**/dashboard')
