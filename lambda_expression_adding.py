def add_n(num: int):
    value = lambda a: a + num
    return value


add_1 = add_n(1)
add_10 = add_n(10)
print(add_1(23))
print(add_10(43))
