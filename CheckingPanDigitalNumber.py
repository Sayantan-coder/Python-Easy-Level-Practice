def is_pandigital(num: int) -> bool:
    num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    number = str(num)
    for num_ in num_list:
        if str(num_) not in number:
            return False
    return True


print(is_pandigital(98140723568910))
print(is_pandigital(90864523148909))
print(is_pandigital(112233445566778899))
