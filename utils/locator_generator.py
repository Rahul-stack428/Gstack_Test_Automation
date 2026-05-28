def generate_locator(element):

    if element["id"]:
        return f'page.locator("#{element["id"]}")'

    elif element["name"]:
        return f'page.locator("[name=\'{element["name"]}\']")'

    elif element["text"]:
        return f'page.get_by_text("{element["text"]}")'

    else:
        return "Locator Not Found"