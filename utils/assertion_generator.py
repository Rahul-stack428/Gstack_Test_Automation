
class AssertionGenerator:

    @staticmethod
    def generate(testcases):

        assertions = []

        for testcase in testcases:

            title = testcase["title"]

            if title == "Valid Login":

                assertions.append({
                    "testcase": title,
                    "assertion":
                    "expect(page).to_have_url('**/dashboard')"
                })

            elif title == "Invalid Password":

                assertions.append({
                    "testcase": title,
                    "assertion":
                    "expect(page.get_by_text('Invalid credentials')).to_be_visible()"
                })

        return assertions
