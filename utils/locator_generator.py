
class LocatorGenerator:

    @staticmethod
    def generate_locator(el):

        if el.get("id"):
            return f'#{el["id"]}'

        if el.get("aria_label"):
            return (
                f'[aria-label='
                f'"{el["aria_label"]}"]'
            )

        if el.get("name"):
            return (
                f'[name="{el["name"]}"]'
            )

        if el.get("placeholder"):
            return (
                f'[placeholder='
                f'"{el["placeholder"]}"]'
            )

        if el.get("role"):
            return (
                f'[role="{el["role"]}"]'
            )

        if el.get("text"):
            return (
                f'text="{el["text"]}"'
            )

        return None

