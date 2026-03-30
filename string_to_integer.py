def str_to_int(string: str) -> int:
    char_list = []
    digit_list = []

    for char in string:
        char_list.append(char)
    for value in char_list:
        digit = ord(value) - ord("0")
        digit_list.append(digit)
    num = 0
    for i in digit_list:
        num = num * 10 + i
    return num


print(str_to_int("4576"))
