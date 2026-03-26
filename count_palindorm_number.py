def count_palindorm(start: int, end: int) -> int:
    # num = ""
    count = 0
    for value in range(start, end + 1):
        value_str = str(value)
        num = ""

        for i in range(len(value_str) - 1, -1, -1):
            num += value_str[i]
        if int(num) == value:
            count += 1
    return count


print(count_palindorm(1, 10))
print(count_palindorm(554, 558))
print(count_palindorm(878, 900))
print(count_palindorm(5, 55))
