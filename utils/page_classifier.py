id="pc4"
class PageClassifier:

    @staticmethod
    def classify(page_map):

        # LOGIN PAGE
        if (
            page_map.get("auth_fields")
            and page_map.get(
                "submit_buttons"
            )
        ):

            return "login_page"

        # DASHBOARD PAGE
        if (
            len(
                page_map.get(
                    "tables",
                    []
                )
            ) > 0
        ):

            return "dashboard_page"

        # FORM PAGE
        if (
            len(
                page_map.get(
                    "inputs",
                    []
                )
            ) > 3
        ):

            return "form_page"

        return "generic_page"
