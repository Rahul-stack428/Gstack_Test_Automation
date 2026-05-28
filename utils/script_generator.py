def generate_pytest_script(url, elements):

    script = f'''
from playwright.sync_api import sync_playwright

def test_generated():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("{url}")

'''

    for el in elements:

        locator = el.get("locator")

        if locator:

            script += f'\n        page.locator("{locator}")'

    script += "\n\n        browser.close()"

    return script