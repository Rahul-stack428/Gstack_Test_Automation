
class LocatorRegistry:

    @staticmethod
    def build(elements):

        registry = {}

        for element in elements:

            name = (
                element.get("name")
                or element.get("placeholder")
                or element.get("text")
                or element.get("id")
            )

            if not name:
                continue

            key = (
                name.lower()
                .replace(" ", "_")
                .replace("-", "_")
            )

            tag = element.get("tag", "")

            if tag == "input":
                variable = f"{key}_input"

            elif tag == "button":
                variable = f"{key}_button"

            elif tag == "select":
                variable = f"{key}_dropdown"

            elif tag == "textarea":
                variable = f"{key}_textarea"

            else:
                variable = key

            registry[key] = variable

        return registry