def int_to_str(num: int) -> str:
    last_digit = []
    char_list = []
    while num > 0:
        digit = num % 10
        last_digit.append(digit)
        num = num // 10
    Last_digit = list(reversed(last_digit))
    for digit in Last_digit:
        char = ord("0") + digit
        char_list.append(chr(char))
    string_value = "".join(char_list)
    return f"{string_value}"


print(int_to_str(2376))
