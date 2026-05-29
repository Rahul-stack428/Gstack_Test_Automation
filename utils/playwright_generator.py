
import os


class PlaywrightGenerator:

    @staticmethod
    def generate(page_data):

        page_type = page_data.get(
            "page_type",
            "generic_page"
        )

        actions = page_data.get(
            "actions",
            []
        )

        assertions = page_data.get(
            "assertions",
            []
        )

        class_name = "".join(
            word.capitalize()
            for word in page_type.split("_")
        )

        filename = (
            f"generated_tests/"
            f"test_{page_type}.py"
        )

        lines = []

        lines.append(
            "from playwright.sync_api "
            "import expect\n"
        )

        lines.append(
            f"from pages.{page_type} "
            f"import {class_name}\n\n"
        )

        test_count = 1

        for action_group in actions:

            testcase_name = (
                action_group["testcase"]
                .lower()
                .replace(" ", "_")
            )

            lines.append(
                f"\ndef test_{testcase_name}"
                f"(page):\n"
            )

            lines.append(
                f"    page_obj = "
                f"{class_name}(page)\n"
            )

            # Actions
            for action in (
                action_group["actions"]
            ):

                if (
                    action["action"]
                    == "fill"
                ):

                    field = (
                        action["field"]
                    )

                    value = (
                        action["value"]
                    )

                    lines.append(
                        f"    page_obj."
                        f"{field}_input"
                        f".fill("
                        f"'{value}')\n"
                    )

                elif (
                    action["action"]
                    == "click"
                ):

                    field = (
                        action["field"]
                    )

                    lines.append(
                        f"    page_obj."
                        f"{field}_button"
                        f".click()\n"
                    )

            # Assertions
            for assertion in assertions:

                if (
                    assertion["testcase"]
                    == action_group[
                        "testcase"
                    ]
                ):

                    lines.append(
                        f"    "
                        f"{assertion['assertion']}"
                        f"\n"
                    )

            test_count += 1

        os.makedirs(
            "generated_tests",
            exist_ok=True
        )

        with open(
            filename,
            "w"
        ) as file:

            file.writelines(lines)

        print(
            f"Generated Test File: "
            f"{filename}"
        )
