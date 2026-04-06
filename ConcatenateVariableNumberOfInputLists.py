def concatenate_list(*list_values: list) -> list:
    concatenate_list = []
    for list_ in list_values:
        for value in list_:
            concatenate_list.append(value)
    return concatenate_list


print(concatenate_list([1, 2, 3], [4, 5], [6, 7]))
print(concatenate_list([1], [2], [3], [4], [5], [6], [7]))
print(concatenate_list([1, 2], [3, 4]))
print(concatenate_list([4, 4, 4, 4, 4]))
