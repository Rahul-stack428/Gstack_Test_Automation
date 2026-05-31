class WorkflowDetector:

    @staticmethod
    def detect(components):

        workflows = []

        component_types = [
            c.get("type")
            for c in components
        ]

        if "login_form" in component_types:
            workflows.append("login")

        if "role_selection" in component_types:
            workflows.append(
                "role_selection"
            )
        if "role_selection" in component_types:
            workflows.append(
                "role_selection"
            )

        return workflows