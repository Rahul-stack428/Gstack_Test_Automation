from bs4 import BeautifulSoup

def extract_elements(html):

    soup = BeautifulSoup(html, "html.parser")

    elements = []

    tags = ["input", "button", "a", "select", "textarea"]

    for tag in tags:

        for el in soup.find_all(tag):

            elements.append({
                "tag": tag,
                "id": el.get("id"),
                "name": el.get("name"),
                "class": el.get("class"),
                "text": el.text.strip()
            })

    return elements