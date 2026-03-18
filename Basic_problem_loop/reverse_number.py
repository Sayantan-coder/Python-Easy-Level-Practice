# def reverse_number(num: int) -> int:
#     temp1 = str(num)
#     store = ""
#     for index in range(len(temp1) - 1, -1, -1):
#         store = store + temp1[index]
#     # new_number = int(store)
#     return store


# ReverseNumber = reverse_number(876534)
# print(ReverseNumber)
# Reverse a number using while loop:-


def reverse_number(num: int) -> int:
    reverse = 0
    while num > 0:
        last_digit = num % 10
        reverse = reverse * 10 + last_digit
        num = num // 10  # Floor Division
    return reverse


ReverseNumber = reverse_number(4567)
print(ReverseNumber)
