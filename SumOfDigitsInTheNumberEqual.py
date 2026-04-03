def is_equal(num_list: list) -> bool:
    sum1 = 0
    sum2 = 0
    num1 = num_list[0]
    num2 = num_list[1]
    while num1:
        digit = num1 % 10
        sum1 += digit
        num1 = num1 // 10
    while num2:
        digit = num2 % 10
        sum2 += digit
        num2 = num2 // 10
    if sum1 == sum2:
        return True
    else:
        return False


print(is_equal([105, 42]))
print(is_equal([21, 35]))
print(is_equal([101, 200]))
