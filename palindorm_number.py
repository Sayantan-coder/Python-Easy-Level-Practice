def is_palindorm(num: int) -> bool:
    num_str = str(num)
    temp = ""
    for i in range(len(num_str) - 1, -1, -1):
        temp += num_str[i]
    value = int(temp)
    if value == num:
        return True
    return False


print(is_palindorm(455454))
print(is_palindorm(1112111))
