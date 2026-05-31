
class TestCaseGenerator:

    @staticmethod
    def generate(components):

        testcases = []

        for component in components:

            component_type = component.get("type")

            # LOGIN FORM
            if component_type == "login_form":

                testcases.extend([
                    {
                        "title": "Valid Login",
                        "category": "positive"
                    },
                    {
                        "title": "Invalid Password",
                        "category": "negative"
                    },
                    {
                        "title": "Invalid Email",
                        "category": "negative"
                    },
                    {
                        "title": "Blank Email",
                        "category": "validation"
                    },
                    {
                        "title": "Blank Password",
                        "category": "validation"
                    }
                ])

            # SEARCH BAR
            elif component_type == "search_bar":

                testcases.extend([
                    {
                        "title": "Valid Search",
                        "category": "positive"
                    },
                    {
                        "title": "No Result Search",
                        "category": "negative"
                    }
                ])

            # DATA TABLE
            elif component_type == "data_table":

                testcases.extend([
                    {
                        "title": "Verify Table Loads",
                        "category": "positive"
                    },
                    {
                        "title": "Verify Pagination",
                        "category": "functional"
                    }
                ])
            elif component_type == "role_selection":

                testcases.extend([
                    {
                        "title": "Select Platform Admin",
                        "category": "positive"
                    }
                ])

        return testcases
