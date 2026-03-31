def dict_inversion(dictionary: dict) -> dict:
    invert_dictionary = {}
    for key, value in dictionary.items():
        invert_dictionary[value] = key
    return invert_dictionary


print(dict_inversion({"z": "q", "w": "f"}))
print(dict_inversion({"a": 1, "b": 2, "c": 3}))
print(dict_inversion({"zebra": "koala", "horse": "camel"}))
