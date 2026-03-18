def factorial(num: int) -> int:
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact


factorial_number = factorial(4)
print(factorial_number)
