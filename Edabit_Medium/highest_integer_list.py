def get_highest_integer(value_list) -> int:
    max = 0
    for num in value_list:
        if num > max:
            max = num
    return max


print(get_highest_integer([-1, 97, 67, -97, 0, 87, 456, -1234]))
print(get_highest_integer([-1, 3, 5, 6, 99, 12, 2]))
print(get_highest_integer([0, 12, 4, 87]))
print(get_highest_integer([8]))


# Using Recursion:-


def get_highest_integer(value_list: list) -> int:
    if len(value_list) == 1:
        return value_list[0]
    else:
        first = value_list[0]
        max_of_rest = get_highest_integer(value_list[1:])

        if max_of_rest > first:
            return max_of_rest
        else:
            return first


print(get_highest_integer([-1, 97, 67, -97, 0, 87, 456, -1234]))
print(get_highest_integer([-1, 3, 5, 6, 99, 12, 2]))
print(get_highest_integer([0, 12, 4, 87]))
print(get_highest_integer([8]))
