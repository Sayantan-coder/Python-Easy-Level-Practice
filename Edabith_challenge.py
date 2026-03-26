def edabith(start: int, end: int) -> list:
    new_list = []
    for num in range(start, end + 1):
        if num == 0:
            new_list.append("EdaBit")
        elif num % 3 == 0 and num % 5 == 0:
            new_list.append("EdaBit")
        elif num % 3 == 0:
            new_list.append("Eda")
        elif num % 5 == 0:
            new_list.append("Bit")
        else:
            new_list.append(num)
    return new_list


print(edabith(4, 25))
print(edabith(0, 10))
print(edabith(14, 20))
print(edabith(100, 106))
