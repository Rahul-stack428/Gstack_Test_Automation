from utils.dom_parser import DOMParser
from utils.role_detector import RoleDetector

with open(
    "doms/role_popup.html",
    "r",
    encoding="utf-8"
) as f:

    html = f.read()

elements = DOMParser.extract_elements(
    html
)

role_component = RoleDetector.detect(
    elements
)

print("\nROLE COMPONENT:")
print(role_component)