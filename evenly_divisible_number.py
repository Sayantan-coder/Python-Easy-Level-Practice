def SumOfEvenlyDivisible(a: int, b: int, c: int) -> int:
    sum = 0
    for num in range(a, b + 1):
        if num % c == 0:
            sum = sum + num

    return sum


print(SumOfEvenlyDivisible(3, 15, 3))
