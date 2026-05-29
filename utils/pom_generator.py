id="pomcode1"
import json
import os


class POMGenerator:

    @staticmethod
    def sanitize_name(name):

        if not name:
            return "unknown"

        return (
            name.lower()
            .replace(" ", "_")
            .replace("-", "_")
            .replace(".", "_")
        )

    @staticmethod
    def generate_page_class(page_data):



        page_type = (
            page_data.get("page_type")
            or "generic_page"
        )

        class_name = "".join(
            word.capitalize()
            for word in page_type.split("_")
        )

        filename = (
            f'pages/{page_type}.py'
        )

        elements = (
            page_data.get("elements", [])
        )

        lines = []

        lines.append(
            "from pages.base_page import BasePage\n"
        )

        lines.append(
            f"\nclass {class_name}(BasePage):\n"
        )

        lines.append(
            "\n    def __init__(self, page):\n"
        )

        lines.append(
            "        super().__init__(page)\n"
        )

        # Generate locators
        for el in elements:

            locator = el.get("locator")

            if not locator:
                continue

            name = (
                el.get("name")
                or el.get("placeholder")
                or el.get("text")
                or el.get("id")
                or "element"
            )

            variable = (
                POMGenerator.sanitize_name(
                    name
                )
            )

            lines.append(
                f'\n        self.{variable}'
                f' = page.locator('
                f'"{locator}")\n'
            )

        
        id = "step5code2"
        workflows = (
            page_data.get(
                "workflows",
                []
            )
        )

        # LOGIN METHOD
        if "login" in workflows:
            lines.append(
                "\n    def login("
                "self, username, password):\n"
            )

            lines.append(
                "        self.email.fill("
                "username)\n"
            )

            lines.append(
                "        self.password.fill("
                "password)\n"
            )

            lines.append(
                "        self.sign_in.click()\n"
            )

            lines.append(
                "        self.page."
                "wait_for_load_state("
                "'networkidle')\n"
            )

        # SEARCH METHOD
        if "search" in workflows:
            lines.append(
                "\n    def search("
                "self, text):\n"
            )

            lines.append(
                "        self.search.fill("
                "text)\n"
            )

            lines.append(
                "        self.search."
                "press('Enter')\n"
            )



    # Generate login method
        if page_type == "login_page":

            lines.append(
                "\n    def login("
                "self, username, password):\n"
            )

            lines.append(
                "        self.email.fill("
                "username)\n"
            )

            lines.append(
                "        self.password.fill("
                "password)\n"
            )

            lines.append(
                "        self.sign_in.click()\n"
            )

        os.makedirs("pages", exist_ok=True)

        with open(filename, "w") as file:

            file.writelines(lines)

        print(
            f'Generated POM: {filename}'
        )
