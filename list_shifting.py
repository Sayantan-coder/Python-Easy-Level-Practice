def list_compare(val1: list, val2: list) -> bool:
    list1 = []
    list2 = []
    for pair in zip(val1, val2):
        list1.append(pair[0])
        list2.append(pair[1])
    if list1[0] == list2[1]:
        return True
    return False


result = list_compare([1, 2, 3, 4, 5], [0, 1, 2, 3, 4])
print(result)
