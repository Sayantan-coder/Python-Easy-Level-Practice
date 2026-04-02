def get_index(list_value: list, value: int):
    index_list = []
    for ind in range(len(list_value)):
        if list_value[ind] == value:
            index_list.append(ind)
    return index_list


print(get_index(["a", "a", "b", "a", "b", "a"], "a"))
print(get_index([1, 5, 5, 2, 7], 7))
print(get_index([1, 5, 5, 2, 7], 5))
print(get_index([1, 5, 5, 2, 7], 8))
