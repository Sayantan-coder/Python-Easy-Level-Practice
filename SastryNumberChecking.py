def is_sastrynumber(number: int) -> bool:
    num = str(number)
    num1 = str(number + 1)
    new_number = int(num + num1)
    square_root_value = int(new_number**0.5)
    if square_root_value * square_root_value == new_number:
        return True
    else:
        return False


print(is_sastrynumber(144))
print(is_sastrynumber(184))
print(is_sastrynumber(106755))
