class RoleSelector:

    @staticmethod
    def select_role(page, role):

        print(f"\nSelecting role: {role}")

        page.get_by_text(role).click()

        page.wait_for_load_state("networkidle")

        page.wait_for_timeout(3000)

        print(f"Current URL: {page.url}")

        print(f"Page Title: {page.title()}")