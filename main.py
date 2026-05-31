id="mainfixed1"
import json

from utils.crawler import get_page_content
from utils.dom_parser import DOMParser
from utils.locator_generator import LocatorGenerator
from utils.deduplicator import Deduplicator
from utils.page_mapper import PageMapper
from utils.page_classifier import PageClassifier
from utils.pom_generator import (POMGenerator)
from utils.test_generator import (TestGenerator)
from utils.component_detector import ComponentDetector
from utils.testcase_generator import (TestCaseGenerator)
from utils.action_generator import (ActionGenerator)
from utils.assertion_generator import (AssertionGenerator)
from utils.locator_registry import (LocatorRegistry)
from utils.playwright_generator import (PlaywrightGenerator)
from utils.role_detector import (RoleDetector)
from utils.workflow_detector import (WorkflowDetector)
from utils.workflow_crawler import (
    WorkflowCrawler
)
from utils.role_page_detector import RolePageDetector

from config import *


browser, context, playwright = (
    WorkflowCrawler.login_and_capture(
        username=USERNAME,
        password=PASSWORD
    )
)
print("Login completed")

print("\nProcessing Role Popup...")

with open(
    "doms/role_popup.html",
    "r",
    encoding="utf-8"
) as f:

    role_html = f.read()

    role_elements = DOMParser.extract_elements(
        role_html
    )

    print(
        "\nRole Elements Found:",
        len(role_elements)
    )

    role_component = (
        RoleDetector.detect(
            role_elements
        )
    )
    print("\nROLE COMPONENT:")
    print(role_component)

    role_components = []

    if role_component:
        role_components.append(
            role_component
        )
    role_workflows = (
        WorkflowDetector.detect(
            role_components
        )
    )

    print(
        "\nRole Workflows:"
    )

    role_testcases = (
        TestCaseGenerator.generate(
            role_components
        )
    )

    print(
        "\nRole Test Cases:"
    )

    print(
        role_testcases
    )

    role_assertions = (
        AssertionGenerator.generate(
            role_testcases
        )
    )

    role_locator_registry = (
        LocatorRegistry.build(
            role_elements
        )
    )

    role_actions = (
        ActionGenerator.generate(
            role_testcases,
            role_components,
            role_locator_registry
        )
    )

    print(
        "\nRole Actions:"
    )

    print(
        role_actions
    )

    role_page_data = {

        "url":
            "role_popup",

        "page_type":
            "role_selection_page",

        "elements":
            role_elements,

        "components":
            role_components,

        "workflows":
            role_workflows,

        "testcases":
            role_testcases,

        "assertions":
            role_assertions,

        "actions":
            role_actions,

        "locator_registry":
            role_locator_registry
    }

    POMGenerator.generate_page_class(
        role_page_data
    )

    PlaywrightGenerator.generate(
        role_page_data
    )

    TestGenerator.generate_test(
        role_page_data
    )

all_pages = []

with open("urls/urls.txt") as f:

    urls = f.readlines()

for url in urls:

    url = url.strip()

    print(f"\nScanning: {url}")

    page = context.new_page()

    page.goto(
        url,
        wait_until="networkidle"
    )
    print(
        f"Requested URL: {url}"
    )

    print(
        f"Actual URL: {page.url}"
    )

    print(
        f"Actual URL: {page.url}"
    )

    html = page.content()
    print("HTML Length:", len(html))

    print("DOM extracted")

    print("\n================================")
    print("CURRENT URL:", url)
    print("HTML LENGTH:", len(html))
    print("================================")
    elements = DOMParser.extract_elements(
        html
    )
    with open(
            "doms/current_debug.html",
            "w",
            encoding="utf-8"
    ) as f:
        f.write(html)

    cleaned_elements = []

    # Generate locators
    for el in elements:

        locator = (
            LocatorGenerator.generate_locator(el)
        )

        if locator:

            el["locator"] = locator

            cleaned_elements.append(el)

    # Remove duplicates
    cleaned_elements = (
        Deduplicator.remove_duplicates(
            cleaned_elements
        )
    )

    locator_registry = (
        LocatorRegistry.build(
            cleaned_elements
        )
    )

    # Map page
    mapped_page = PageMapper.map_page(
        cleaned_elements
    )

    components = ComponentDetector.detect(
        mapped_page
    )
    if RolePageDetector.is_role_page(html):
        components.append({
            "type": "role_selection"
        })

    print("\nDEBUG VARIABLES")

    print("cleaned_elements exists:",
          "cleaned_elements" in locals())

    print("role_elements exists:",
          "role_elements" in locals())





    print(
        role_workflows
    )

    print("\n========== ROLE DETECTION ==========")
    print(role_component)
    print("====================================")




    if role_component:
        components.append(
            role_component
        )

    if RolePageDetector.is_role_page(html):
        components.append({
            "type": "role_selection",
            "roles": [
                "Platform Admin"
            ]
        })
    workflows = (
        WorkflowDetector.detect(
            components
        )
    )

    print(
        "\nWORKFLOWS:",
        workflows
    )


    testcases = TestCaseGenerator.generate(
        components
    )

    print("Generated Test Cases:")
    print(testcases)

    workflows = (
        PageMapper.detect_workflows(
            mapped_page
        )
    )

    assertions = AssertionGenerator.generate(
        testcases
    )

    print("Generated Assertions:")
    print(assertions)

    actions = ActionGenerator.generate(
        testcases,
        components,
        locator_registry
    )

    print("Generated Actions:")
    print(actions)

    # Classify page
    page_type = (
        PageClassifier.classify(
            mapped_page
        )
    )
    print("\nMAPPED PAGE:")
    print(mapped_page)

    print("\nCOMPONENTS:")
    print(components)


    page_data = {
        "url": url,
        "page_type": page_type,
        "elements": cleaned_elements,
        "page_map": mapped_page,
        "workflows": workflows,
        "components": components,
        "testcases": testcases,
        "assertions": assertions,
        "actions": actions,
        "locator_registry": locator_registry
    }

    POMGenerator.generate_page_class(page_data)
    PlaywrightGenerator.generate(page_data)
    print("Calling TestGenerator")
    TestGenerator.generate_test(page_data)
    print("Test Generated")

    all_pages.append(page_data)

with open(
    "locators/extracted_dom.json",
    "w"
) as file:

    json.dump(
        all_pages,
        file,
        indent=4
    )
    browser.close()
    playwright.stop()

print("\nDOM Extraction Completed")
print(locator_registry)
print("\nCOMPONENTS:")
print(components)
print(workflows)
