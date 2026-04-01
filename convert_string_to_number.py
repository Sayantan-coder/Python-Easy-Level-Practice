def convert_to_number(items: dict) -> dict:
    modified_items = {}
    for key in items.keys():
        value = int(items[key])
        modified_items[key] = value
    return modified_items


print(convert_to_number({"piano": "200"}))
print(convert_to_number({"piano": "200", "tv": "300"}))
print(convert_to_number({"piano": "200", "tv": "300", "stereo": "400"}))
