def get_binary(num: int):
    bit_list = []
    binary_list = []
    while num > 0:
        bit = num % 2
        bit_list.append(bit)
        num = num // 2
    for i in range(len(bit_list) - 1, -1, -1):
        binary_list.append(bit_list[i])
    binary_number = "".join(str(num) for num in binary_list)
    return binary_number


print(get_binary(10))

print(get_binary(7))
print(get_binary(15))
