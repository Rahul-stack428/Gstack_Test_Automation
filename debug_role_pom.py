from utils.pom_generator import POMGenerator

page_data = {
    "url": "role_popup",
    "page_type": "role_selection_page",
    "components": [
        {
            "type": "role_selection"
        }
    ]
}

POMGenerator.generate_page_class(
    page_data
)