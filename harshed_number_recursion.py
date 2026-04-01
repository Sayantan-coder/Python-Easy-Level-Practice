def harshed_number(num: int) -> bool:
    number = str(num)

    def get_sum_of_digits(number):
        if len(number) == 1:
            return number[0]
        else:
            first_digit = number[0]
            sum_rest_of_digit = get_sum_of_digits(number[1:])
            sum_digits = int(first_digit) + int(sum_rest_of_digit)
            return sum_digits

    sum = get_sum_of_digits(number)
    if num % sum == 0:
        return True
    else:
        return False


print(harshed_number(481))
print(harshed_number(89))
print(harshed_number(516))
print(harshed_number(200))
