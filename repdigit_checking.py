def is_repdigit(num: int) -> bool:
    if num < 0:
        return False
    else:
        if num == 0:
            return True
        else:
            last_digit = num % 10
            num = num // 10
            second_last_digit = num % 10
            if last_digit == second_last_digit:
                return True
            else:
                return False


print(is_repdigit(3333))
print(is_repdigit(112211))
print(is_repdigit(0))
print(is_repdigit(-333))
