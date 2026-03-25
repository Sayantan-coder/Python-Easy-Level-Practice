def update_list(value: list) -> list:
    new_list = []
    for i in value:
        if type(i) == int:
            new_list.append(i)
    return new_list


print(update_list([34, 56.8, 23, "G", "34", 0.8]))
