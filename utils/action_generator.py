
class ActionGenerator:

    @staticmethod
    def generate(testcases,components,locator_registry):

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
                                        "locator_var":
                                            locator_registry.get(
                                                "email"
                                            ),
                                        "value_key":
                                            "valid_email"
                                    },

                                    {
                                        "action": "fill",
                                        "field": "password",
                                        "locator_var":
                                            locator_registry.get(
                                                "password"
                                            ),
                                        "value_key":
                                            "valid_password"
                                    },

                                    {
                                        "action": "click",
                                        "field": "sign_in",
                                        "locator_var":
                                            locator_registry.get(
                                                "sign_in"
                                            )
                                    }
                                ]

                elif title == "Invalid Password":

                    action_set = [
                                  {
                                    "action": "fill",
                                    "field": "email",
                                    "locator_var": locator_registry.get(
                                                "email"),
                                    "value_key": "valid_email"
                                  },
                                  {
                                    "action": "fill",
                                    "field": "password",
                                    "locator_var": locator_registry.get(
                                                "password"),
                                    "value_key": "invalid_password"
                                  },
                                  {
                                    "action": "click",
                                    "field": "sign_in",
                                    "locator_var": locator_registry.get(
                                                "sign_in")
                                  }
                                ]
                elif title == "Select Platform Admin":

                    action_set = [
                    {
                        "action": "click",
                        "field": "platform_admin"
                    }
                ]

            actions.append({
                "testcase": title,
                "actions": action_set
            })

        return actions
