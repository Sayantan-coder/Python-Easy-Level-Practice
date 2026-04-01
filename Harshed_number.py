def is_harshed(num: int) -> bool:
    sum_of_num = 0
    number = num
    while num:
        last_digit = num % 10
        sum_of_num += last_digit
        num = num // 10
    if number % sum_of_num == 0:
        return True
    else:
        return False

    # return sum_of_num


print(is_harshed(172))
print(is_harshed(481))
print(is_harshed(89))
print(is_harshed(516))
print(is_harshed(200))
