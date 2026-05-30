class RoleDetector:

    @staticmethod
    def detect(elements):

        texts = []

        for element in elements:

            text = (
                element.get("text", "")
                .strip()
                .lower()
            )

            if text:
                texts.append(text)

        if (
            "platform admin" in texts
            or
            "tenant" in texts
        ):
            return {
                "type": "role_selection"
            }

        return None