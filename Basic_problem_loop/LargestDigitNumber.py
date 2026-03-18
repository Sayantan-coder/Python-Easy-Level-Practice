def largest_digit(num: int) -> int:
    max_digit = 0
    while num > 0:
        last_digit = num % 10
        num = num // 10
        if last_digit > max_digit:
            max_digit = last_digit
    return max_digit


MaximumDigit = largest_digit(5678)
print(MaximumDigit)
