def sum_missing_number(num_list: list) -> int:
    def get_max_number(num_list):
        if len(num_list) == 1:
            return num_list[0]
        else:
            max = num_list[0]
            rest_max = get_max_number(num_list[1:])
            if max > rest_max:
                return max
            else:
                return rest_max

    def get_min_number(num_list):
        if len(num_list) == 1:
            return num_list[0]
        else:
            min = num_list[0]
            rest_min = get_min_number(num_list[1:])
            if min < rest_min:
                return min
            else:
                return rest_min

    max_value = get_max_number(num_list)
    min_value = get_min_number(num_list)
    missing_num_list = []

    full_list = [num for num in range(min_value, max_value + 1)]
    sum = 0
    for ind in range(len(full_list)):
        if full_list[ind] not in num_list:
            missing_num_list.append(full_list[ind])
    if missing_num_list:

        def get_sum(missing_num_list):
            if len(missing_num_list) == 1:
                return missing_num_list[0]
            else:
                first = missing_num_list[0]
                rest = get_sum(missing_num_list[1:])
                sum = first + rest
                return sum

    else:
        return sum
    return get_sum(missing_num_list)


print(sum_missing_number([17, 16, 15, 10, 11, 12]))
print(sum_missing_number([4, 3, 8, 1, 2]))
print(sum_missing_number([1, 2, 3, 4, 5]))
