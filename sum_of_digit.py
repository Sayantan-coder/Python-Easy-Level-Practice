def sum_digit(num: int) -> int:
    sum = 0
    while num > 0:
        last_digit = num % 10
        sum = sum + last_digit
        num = num // 10  # Floor Division
    return sum


sum_of_digits = sum_digit(34567)
print(sum_of_digits)
