def list_of_multiple(num: int, length: int) -> list:
    multiple_list = []

    for i in range(1, length + 1):
        result = num * i
        multiple_list.append(result)
    return multiple_list


print(list_of_multiple(19, 10))
print(list_of_multiple(7, 5))
print(list_of_multiple(12, 10))
print(list_of_multiple(13, 6))
