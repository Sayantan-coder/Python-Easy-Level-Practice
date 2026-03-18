def is_palindorm(num) -> bool:

    temp1 = str(num)

    temp2 = ""
    for i in range(len(temp1) - 1, -1, -1):
        temp2 = temp2 + temp1[i]
        print(temp2)

    if temp1 == temp2:
        return True
    else:
        return False


check_palindorm = is_palindorm(354453)
print(check_palindorm)
