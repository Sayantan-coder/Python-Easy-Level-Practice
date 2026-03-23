def DecimalToBinary(num: int):
    List = []
    if num == 0:
        return 0
    while num > 0:
        remainder = num % 2
        num = num // 2
        List.append(remainder)
    reverse_list = [List[i] for i in range(len(List) - 1, -1, -1)]
    result = "".join(str(i) for i in reverse_list)
    return result


Binary_Conversion = DecimalToBinary(50)
print(Binary_Conversion)
