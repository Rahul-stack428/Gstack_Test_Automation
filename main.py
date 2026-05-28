import json

from utils.crawler import get_page_content
from utils.dom_parser import extract_elements
from utils.locator_generator import generate_locator
from utils.ai_engine import generate_testcases
from utils.script_generator import generate_pytest_script

with open("urls/urls.txt") as f:
    urls = f.readlines()

for url in urls:

    url = url.strip()

    print(f"Processing: {url}")

    html = get_page_content(url)

    elements = extract_elements(html)

    for el in elements:
        el["locator"] = generate_locator(el)

    with open("locators/extracted_locators.json", "w") as file:
        json.dump(elements, file, indent=4)

    print("Locators extracted")

    testcases = generate_testcases(elements)

    with open("testcases/generated_testcases.txt", "w") as file:
        file.write(testcases)

    print("Test cases generated")

    script = generate_pytest_script(url, elements)

    with open("generated_tests/test_generated.py", "w") as file:
        file.write(script)

    print("Automation script generated")