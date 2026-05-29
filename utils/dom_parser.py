
from bs4 import BeautifulSoup


class DOMParser:

    IMPORTANT_TAGS = [
        "input",
        "button",
        "textarea",
        "select",
        "a",
        "table",
        "form"
    ]

    @staticmethod
    def clean_dom(html):

        soup = BeautifulSoup(
            html,
            "html.parser"
        )

        for tag in soup(
            ["script", "style", "svg", "noscript"]
        ):
            tag.decompose()

        return soup

    @staticmethod
    def extract_elements(html):

        soup = DOMParser.clean_dom(html)

        elements = []

        for tag in DOMParser.IMPORTANT_TAGS:

            for el in soup.find_all(tag):

                element = {
                    "tag": tag,
                    "id": el.get("id"),
                    "name": el.get("name"),
                    "type": el.get("type"),
                    "placeholder": el.get(
                        "placeholder"
                    ),
                    "aria_label": el.get(
                        "aria-label"
                    ),
                    "role": el.get("role"),
                    "text": el.text.strip(),
                    "class": el.get("class")
                }

                elements.append(element)

        return elements

