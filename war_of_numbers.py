def war_of_number(num: list) -> int:
    sum_odd = 0
    sum_even = 0
    for i in num:
        if i % 2 == 0:
            sum_even += i
        else:
            sum_odd += i
    if sum_odd > sum_even:
        return sum_odd - sum_even
    else:
        return sum_even - sum_odd


print(war_of_number([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]))
