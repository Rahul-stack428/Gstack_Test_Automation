from playwright.sync_api import sync_playwright
from utils.role_page_detector import RolePageDetector
import os



class WorkflowCrawler:

    @staticmethod
    def login_and_capture(
            username,
            password
    ):
        print(
            f"Username received: {username}"
        )

        print(
            f"Password received: {password}"
        )


        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=False
            )

            context = browser.new_context()

            page = context.new_page()

            print("\nOpening login page...")

            page.goto(
                "https://admin-test.granitestack.ai/admin/login",
                wait_until="networkidle"
            )

            # Capture Login Page DOM
            with open(
                    "doms/login_page.html",
                    "w",
                    encoding="utf-8"
            ) as file:

                file.write(
                    page.content()
                )

            print("Entering credentials...")

            email_field = page.locator(
                '[name="email"]'
            )

            email_field.fill(username)

            print(
                "Email after fill:",
                email_field.input_value()
            )

            password_field = page.locator(
                '[name="password"]'
            )

            password_field.fill(password)

            print(
                "Password after fill:",
                password_field.input_value()
            )

            print("Email value:",
                  page.locator(
                      '[name="email"]'
                  ).input_value())

            print("Password value:",
                  page.locator(
                      '[name="password"]'
                  ).input_value())

            sign_in_btn = page.locator(
                'button[type="submit"]'
            )

            print(
                "Button Enabled:",
                sign_in_btn.is_enabled()
            )

            page.screenshot(
                path="doms/before_click.png",
                full_page=True
            )

            print("Clicking Sign In")

            sign_in_btn.click()

            page.wait_for_timeout(
                5000
            )

            print(
                "Current URL:",
                page.url
            )

            print(
                "Page Title:",
                page.title()
            )

            print(
                f"\nCurrent URL: {page.url}"
            )

            page.screenshot(
                path="doms/post_login.png",
                full_page=True
            )

            html = page.content()

            # Detect Role Page
            if RolePageDetector.is_role_page(
                    html
            ):

                print(
                    "\nROLE PAGE DETECTED"
                )

                with open(
                        "doms/role_selection.html",
                        "w",
                        encoding="utf-8"
                ) as file:

                    file.write(html)

                print(
                    "Role page saved"
                )

                try:

                    print(
                        "\nSelecting Platform Admin..."
                    )

                    page.get_by_text(
                        "Platform Admin"
                    ).click()

                    page.wait_for_load_state(
                        "networkidle"
                    )

                    page.wait_for_timeout(
                        3000
                    )

                    dashboard_html = (
                        page.content()
                    )

                    with open(
                            "doms/dashboard.html",
                            "w",
                            encoding="utf-8"
                    ) as file:

                        file.write(
                            dashboard_html
                        )

                    page.screenshot(
                        path=
                        "doms/dashboard.png",
                        full_page=True
                    )

                    print(
                        "\nDashboard captured"
                    )

                    print(
                        f"Dashboard URL: "
                        f"{page.url}"
                    )

                except Exception as e:

                    print(
                        f"\nRole selection failed:"
                        f" {e}"
                    )

            else:

                print(
                    "\nROLE PAGE NOT DETECTED"
                )

                with open(
                        "doms/post_login.html",
                        "w",
                        encoding="utf-8"
                ) as file:

                    file.write(html)

            browser.close()

            return html