from utils.dom_parser import DOMParser
from utils.role_detector import RoleDetector
from utils.workflow_detector import WorkflowDetector
from utils.testcase_generator import TestCaseGenerator

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

components = []

if role_component:
    components.append(
        role_component
    )

print("\nCOMPONENTS:")
print(components)

workflows = WorkflowDetector.detect(
    components
)

print("\nWORKFLOWS:")
print(workflows)

testcases = TestCaseGenerator.generate(
    components
)

print("\nTEST CASES:")
print(testcases)