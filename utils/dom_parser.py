
from bs4 import BeautifulSoup


class DOMParser:
    IMPORTANT_TAGS = [
        "input",
        "button",
        "textarea",
        "select",
        "a",
        "table",
        "form",
        "span",
        "label"
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
                text = el.text.strip()

                if (
                        tag in ["span", "label"]
                        and len(text) < 3
                ):
                    continue

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
                    "text": text,
                    "class": el.get("class"),

                }

                elements.append(element)

        print("Buttons Found:",
              len(soup.find_all("button")))

        print("Inputs Found:",
              len(soup.find_all("input")))

        print("Links Found:",
              len(soup.find_all("a")))

        platform_admin_found = any(
            e.get("text", "").lower() == "platform admin"
            for e in elements
        )

        print(
            "Platform Admin Found:",
            platform_admin_found
        )

        role_texts = [
            e.get("text")
            for e in elements
            if e.get("text")
        ]

        print(
            "Role Keywords Found:",
            [
                t for t in role_texts
                if "platform" in t.lower()
                   or "tenant" in t.lower()
            ]
        )

        radio_inputs = [
            e for e in elements
            if e.get("type") == "radio"
        ]

        print(
            "Radio Inputs Found:",
            len(radio_inputs)
        )
        return elements

