
class ComponentDetector:

    @staticmethod
    def detect(page_map):

        components = []

        inputs = page_map.get("inputs", [])
        buttons = page_map.get("buttons", [])

        input_names = [
            (i.get("name") or "").lower()
            for i in inputs
        ]

        button_texts = [
            (b.get("text") or "").lower()
            for b in buttons
        ]
        link_texts = [
            (l.get("text") or "").lower()
            for l in page_map.get("links", [])
        ]

        # LOGIN FORM
        if (
            "email" in input_names
            and "password" in input_names
        ):
            components.append({
                "type": "login_form",
                "fields": [
                    "email",
                    "password"
                ],
                "actions": [
                    "sign_in"
                ]
            })

        # SEARCH BAR
        if any(
            "search" in name
            for name in input_names
        ):
            components.append({
                "type": "search_bar"
            })

        # TABLE
        if len(page_map.get("tables", [])) > 0:
            components.append({
                "type": "data_table"
            })

        all_text = button_texts + link_texts

        if any(
                "platform admin" in text
                for text in all_text
        ):
            components.append({
                "type": "role_selector",
                "roles": [
                    "Platform Admin"
                ]
            })
        print("\nDETECTED COMPONENTS:")
        print(components)

        return components
