def count(list_value: list) -> int:
    list1 = [2, 3, 4, 5, 6]
    list2 = [10, "A", "Q", "J", "K"]
    count = 0
    for value in list_value:
        if value in list1:
            count += 1
        if value in list2:
            count -= 1
    return count


print(count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]))
