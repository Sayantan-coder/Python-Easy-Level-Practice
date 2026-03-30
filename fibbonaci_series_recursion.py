def get_fibbonaci(num: int):
    if num == 0 or num == 1:

        return num
    else:
        next = get_fibbonaci(num - 1) + get_fibbonaci(num - 2)
        return next


fibbonaci_series = get_fibbonaci(1)
print(fibbonaci_series)
