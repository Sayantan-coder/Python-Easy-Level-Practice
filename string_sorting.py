def get_sort_string(name: str) -> str:
    name_list = list(name.lower())
    sorted_list = sorted(name_list)
    sorted_name = "".join(sorted_list)
    return sorted_name


print(get_sort_string("PythON"))
