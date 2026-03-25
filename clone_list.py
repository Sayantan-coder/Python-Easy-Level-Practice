def clone_list(list_value: list) -> list:
    new_list = [i for i in list_value]
    new_list.append(list_value)
    return new_list


print(clone_list(["x", 1, 45, {"name": "deep"}, "mango", 98]))
