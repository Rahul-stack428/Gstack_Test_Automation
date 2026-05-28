import json

with open("locators/extracted_locators.json") as f:
    data = json.load(f)

with open("pages/generated_page.py", "w") as file:

    file.write("class GeneratedPage:\n\n")

    file.write("    def __init__(self, page):\n")
    file.write("        self.page = page\n\n")

    for item in data:

        if item.get("id"):

            variable = item["id"].replace("-", "_")

            file.write(
                f'    {variable} = "{item["locator"]}"\n'
            )

print("POM generated successfully")