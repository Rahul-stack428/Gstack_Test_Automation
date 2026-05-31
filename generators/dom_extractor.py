from playwright.sync_api import sync_playwright


def extract_login_dom():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto(
            "https://admin-test.granitestack.ai/admin/login"
        )

        page.wait_for_load_state("networkidle")

        html = page.content()

        with open(
            "doms/login.html",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(html)

        browser.close()


if __name__ == "__main__":
    extract_login_dom()