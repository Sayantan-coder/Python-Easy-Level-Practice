def find_missing_number(List: list) -> int:
    num_list = [i for i in range(1, 11)]
    value1 = sum(num_list)
    value2 = sum(List)
    missing_number = value1 - value2
    return missing_number


print(find_missing_number([1, 7, 3, 4, 9, 2, 8, 5, 10]))
