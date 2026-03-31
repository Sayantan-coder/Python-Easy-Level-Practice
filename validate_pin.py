def is_validate(pin: str) -> bool:
    char_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for char in pin:
        if char not in char_list:
            return False
    count = 0
    while pin:
        count += 1
        pin = pin[1:]
    if count == 4 or count == 6:
        return True
    else:
        return False


print(is_validate("1234"))
print(is_validate("45135"))
print(is_validate("89abc1"))
print(is_validate("900876"))
print(is_validate(" 4983"))
