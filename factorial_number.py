def fact(num: int) -> int:
    result = 1
    for Num in range(1, num + 1):
        result = result * Num
    return result


factorial_of_number = fact(10)
print(factorial_of_number)
