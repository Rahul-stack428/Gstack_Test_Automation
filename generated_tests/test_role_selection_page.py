from playwright.sync_api import expect
from utils.data_loader import DataLoader
from pages.role_selection_page import RoleSelectionPage


def test_select_platform_admin(page):
    page_obj = RoleSelectionPage(page)
    data = DataLoader.load('login_data.json')
    expect(page).to_have_url('**/dashboard')
