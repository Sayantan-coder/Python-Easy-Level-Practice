def is_parallel(value1: list, value2: list) -> bool:
    if value1[1] != 0 and value2[1] != 0:
        slope1 = value1[0] // value1[1]
        slope2 = value2[0] // value2[1]
        if slope1 == slope2:
            return True
        else:
            return False
    else:
        if value1[0] == value2[0] and value1[1] == value2[1]:
            return True
        else:
            return False


print(is_parallel([1, 2, 3], [1, 2, 4]))
print(is_parallel([2, 4, 1], [4, 2, 1]))
print(is_parallel([0, 1, 5], [0, 1, 5]))
