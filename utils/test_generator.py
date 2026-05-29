id="step6code1"
import os


class TestGenerator:

    @staticmethod
    def generate_test(page_data):

        page_type = (
            page_data.get("page_type")
        )

        workflows = (
            page_data.get(
                "workflows",
                []
            )
        )

        class_name = "".join(
            word.capitalize()
            for word in page_type.split("_")
        )

        filename = (
            f'tests/test_{page_type}.py'
        )

        lines = []

        lines.append(
            f'from pages.'
            f'{page_type} import '
            f'{class_name}\n\n'
        )

        # LOGIN TEST
        if "login" in workflows:

            lines.append(
                "def test_login("
                "authenticated_page):\n"
            )

            lines.append(
                "    page = "
                "authenticated_page\n"
            )

            lines.append(
                f'    page_obj = '
                f'{class_name}(page)\n'
            )

            lines.append(
                "    page_obj.login("
                "'admin@test.com',"
                "'password')\n"
            )

        # SEARCH TEST
        if "search" in workflows:

            lines.append(
                "\ndef test_search("
                "authenticated_page):\n"
            )

            lines.append(
                "    page = "
                "authenticated_page\n"
            )

            lines.append(
                f'    page_obj = '
                f'{class_name}(page)\n'
            )

            lines.append(
                "    page_obj.search("
                "'Playwright')\n"
            )

        os.makedirs(
            "tests",
            exist_ok=True
        )

        with open(filename, "w") as file:

            file.writelines(lines)

        print(
            f'Generated Test: {filename}'
        )
