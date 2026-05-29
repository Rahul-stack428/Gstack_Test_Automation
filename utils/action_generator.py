
class ActionGenerator:

    @staticmethod
    def generate(testcases, components):

        actions = []

        component_types = [
            c.get("type")
            for c in components
        ]

        for testcase in testcases:

            title = testcase.get("title")

            action_set = []

            # LOGIN
            if (
                "login_form"
                in component_types
            ):

                if title == "Valid Login":

                    action_set = [
                        {
                            "action": "fill",
                            "field": "email",
                            "value": "valid_email"
                        },
                        {
                            "action": "fill",
                            "field": "password",
                            "value": "valid_password"
                        },
                        {
                            "action": "click",
                            "field": "sign_in"
                        }
                    ]

                elif title == "Invalid Password":

                    action_set = [
                        {
                            "action": "fill",
                            "field": "email",
                            "value": "valid_email"
                        },
                        {
                            "action": "fill",
                            "field": "password",
                            "value": "invalid_password"
                        },
                        {
                            "action": "click",
                            "field": "sign_in"
                        }
                    ]

            actions.append({
                "testcase": title,
                "actions": action_set
            })

        return actions
