def check_parity(num: int) -> bool:
    is_odd = 1
    Is_Odd = 1
    if 0 < num < 9:
        if num % 2 == 0:
            is_odd = 0
        if is_odd == Is_Odd:
            return True
        else:
            return False
    else:
        if num % 2 == 0:
            is_odd = 0
        num_list = list(str(num))
        value = sum(int(i) for i in num_list)
        if value % 2 == 0:
            Is_Odd = 0
        if is_odd == Is_Odd:
            return True
        else:
            return False


Parity_calculation = check_parity(555)
print(Parity_calculation)
