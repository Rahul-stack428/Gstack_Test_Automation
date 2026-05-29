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


all_pages = []

with open("urls/urls.txt") as f:

    urls = f.readlines()

for url in urls:

    url = url.strip()

    print(f"\nScanning: {url}")

    html = get_page_content(url)

    elements = DOMParser.extract_elements(
        html
    )

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

    # Map page
    mapped_page = PageMapper.map_page(
        cleaned_elements
    )

    workflows = (
        PageMapper.detect_workflows(
            mapped_page
        )
    )

    # Classify page
    page_type = (
        PageClassifier.classify(
            mapped_page
        )
    )

    page_data = {
        "url": url,
        "page_type": page_type,
        "elements": cleaned_elements,
        "page_map": mapped_page,
        "workflows": workflows
    }

    all_pages.append(page_data)

    POMGenerator.generate_page_class(page_data)
    page_data = {
        "url": url,
        "page_type": page_type,
        "elements": cleaned_elements,
        "page_map": mapped_page
    }

    POMGenerator.generate_page_class(
        page_data
    )

    all_pages.append(page_data)

    TestGenerator.generate_test(
        page_data
    )

with open(
    "locators/extracted_dom.json",
    "w"
) as file:

    json.dump(
        all_pages,
        file,
        indent=4
    )

print("\nDOM Extraction Completed")
