def square_digit(num: int) -> int:
    num_str = str(num)
    temp = ""
    for i in num_str:
        temp += str(int(i) ** 2)
    number = int(temp)
    return number


print(square_digit(9119))
print(square_digit(2483))
print(square_digit(3212))
