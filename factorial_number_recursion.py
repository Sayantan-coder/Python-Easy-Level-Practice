def get_factorial(num: int) -> int:
    if num == 0 or num == 1:
        return 1
    else:
        factorial = num * get_factorial(num - 1)
        return factorial


Result = get_factorial(10)
print(Result)
