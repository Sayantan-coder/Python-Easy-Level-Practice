def get_length(num: int) -> int:
    length = 0
    while num > 0:
        last_digit = num % 10
        num = num // 10
        length += 1
    return length


print(get_length(100))
print(get_length(1234))
print(get_length(87))
