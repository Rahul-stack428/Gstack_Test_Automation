
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
            "from utils.data_loader import DataLoader\n"
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

            lines.append(
                "    data = DataLoader.load('login_data.json')\n"
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

                    locator = action["locator_var"]
                    value_key = action["value_key"]

                    lines.append(
                        f"    page_obj.fill("
                        f"page_obj.{locator}, "
                        f"data['{value_key}'])\n"
                    )

                elif (
                    action["action"]
                    == "click"
                ):

                    locator = action["locator_var"]

                    lines.append(
                        f"    page_obj.click("
                        f"page_obj.{locator})\n"
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
