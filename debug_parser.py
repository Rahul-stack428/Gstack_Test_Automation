# debug_parser.py

from utils.dom_parser import DOMParser

with open(
    "doms/role_popup.html",
    "r",
    encoding="utf-8"
) as f:
    html = f.read()

elements = DOMParser.extract_elements(html)

print(
    "Total Elements:",
    len(elements)
)