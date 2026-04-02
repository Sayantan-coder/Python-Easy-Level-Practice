def is_ultimate(num1: int, num2: int, num3: int) -> bool:
    result = num1 * num2
    result_last_digit = result % 10
    num3_last_digit = num3 % 10
    if result_last_digit == num3_last_digit:
        return True
    return False


print(is_ultimate(25, 21, 125))
print(is_ultimate(55, 226, 5190))
print(is_ultimate(12, 215, 2142))
print(is_ultimate(5, -4, 130))
