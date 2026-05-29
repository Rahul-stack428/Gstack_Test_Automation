id="mappercode1"
class PageMapper:

    @staticmethod
    def map_page(elements):

        page_map = {
            "forms": [],
            "buttons": [],
            "inputs": [],
            "dropdowns": [],
            "links": [],
            "tables": [],
            "textareas": []
        }

        for el in elements:

            tag = el.get("tag")

            text = (
                el.get("text") or ""
            ).lower()

            role = (
                el.get("role") or ""
            ).lower()

            input_type = (
                el.get("type") or ""
            ).lower()

            # INPUTS
            if tag == "input":

                page_map["inputs"].append(el)

                if (
                    input_type == "password"
                ):

                    page_map.setdefault(
                        "auth_fields",
                        []
                    ).append(el)

            # BUTTONS
            elif tag == "button":

                page_map["buttons"].append(el)

                if (
                    "submit" in text
                    or "login" in text
                    or "sign in" in text
                ):

                    page_map.setdefault(
                        "submit_buttons",
                        []
                    ).append(el)

            # DROPDOWNS
            elif tag == "select":

                page_map[
                    "dropdowns"
                ].append(el)

            # LINKS
            elif tag == "a":

                page_map["links"].append(el)

            # TABLES
            elif tag == "table":

                page_map["tables"].append(el)

            # TEXTAREA
            elif tag == "textarea":

                page_map[
                    "textareas"
                ].append(el)

        return page_map

    id="step5code1"
    @staticmethod
    def detect_workflows(page_map):

        workflows = []

        inputs = (
            page_map.get("inputs", [])
        )

        buttons = (
            page_map.get("buttons", [])
        )

        input_names = [
            (
                el.get("name")
                or ""
            ).lower()
            for el in inputs
        ]

        button_texts = [
            (
                el.get("text")
                or ""
            ).lower()
            for el in buttons
        ]

        # LOGIN FLOW
        if (
            "email" in input_names
            and "password" in input_names
        ):

            workflows.append("login")

        # SEARCH FLOW
        if any(
            "search" in name
            for name in input_names
        ):

            workflows.append("search")

        # CREATE FLOW
        if any(
            "create" in text
            for text in button_texts
        ):

            workflows.append(
                "create_entity"
            )

        return workflows
