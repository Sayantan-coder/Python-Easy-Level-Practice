def get_sum_fraction(value: list) -> int:
    sum = 0
    for element in value:
        sum = sum + (element[0] / element[1])
    return f"{sum:.0f}"


print(get_sum_fraction([[18, 13], [4, 5]]))
print(get_sum_fraction([[36, 4], [22, 60]]))
print(get_sum_fraction([[11, 2], [3, 4], [5, 4], [21, 11], [12, 6]]))
