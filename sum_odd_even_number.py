def sum_odd_even(value_list: list) -> list:
    sum_odd = 0
    sum_even = 0
    for num in value_list:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num
    result = [sum_even, sum_odd]
    return result


print(sum_odd_even([1, 2, 3, 4, 5, 6]))
print(sum_odd_even([-1, -2, -3, -4, -5, -6]))
print(sum_odd_even([0, -5, -6, 0]))
