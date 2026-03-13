import math


def DigitCount(num: int) -> int:
    Result = num
    count = 0
    while Result > 0:
        Result = math.floor(Result / 10)
        count = count + 1

    return count


number_of_digit = DigitCount(56789)
print(f"Number of digit is:{number_of_digit}")
