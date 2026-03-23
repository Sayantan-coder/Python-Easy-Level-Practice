def count_one(num: int) -> int:
    list = []
    count = 0
    while num > 0:
        remainder = num % 2
        num = num // 2
        list.append(remainder)
    binary_list = [list[i] for i in range(len(list) - 1, -1, -1)]
    binary_string = "".join(str(i) for i in binary_list)
    print(binary_string)
    for i in binary_string:
        if i == "1":
            count = count + 1
    return count


print(count_one(15))
