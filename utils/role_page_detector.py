class RolePageDetector:

    @staticmethod
    def is_role_page(html):

        html = html.lower()

        role_keywords = [
            "platform admin",
            "tenant"
        ]

        matches = 0

        for keyword in role_keywords:

            if keyword in html:
                matches += 1

        return matches >= 2