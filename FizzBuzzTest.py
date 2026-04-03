def fizz_buzz(num: int) -> list:
    result_list = []
    for value in range(1, num + 1):
        if value % 15 == 0:
            result_list.append("FizzBuzz")
        elif value % 5 == 0:
            result_list.append("Buzz")
        elif value % 3 == 0:
            result_list.append("Fizz")
        else:
            result_list.append(value)
    return result_list


print(fizz_buzz(10))
print(fizz_buzz(20))
print(fizz_buzz(7))
