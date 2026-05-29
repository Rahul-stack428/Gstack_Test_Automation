from pages.login_page import LoginPage

def test_login(authenticated_page):
    page = authenticated_page
    page_obj = LoginPage(page)
    page_obj.login('admin@test.com','password')
