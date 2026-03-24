def add_index(List: list) -> list:
    new_List = [List[i] + i for i in range(0, len(List))]
    return new_List


print(add_index([12, 3, 2, 5, 7, 8]))
